import os
import argparse
import re

import jinja2
from markdown import markdown as mdRenderer
from ruamel.yaml import YAML


yaml = YAML(typ='safe')
yaml.default_flow_style = False

def markdown(text):
    p = re.compile('(!\[[^]]*]\()')
    return mdRenderer(p.sub(r'\1../medias/', text), extensions=["markdown.extensions.extra"])

def markdownrp(text):
    return markdown(text)[3:-4]

def getYaml(path):
    with open(path) as f:
        return yaml.load(f)

def dumpYaml(path, data):
    with open(path, 'w') as f:
        yaml.dump(data, f)

def getTemplates():
    def filterTemplates(fn):
        if 'partials/' not in fn:
            return True

    templateLoader = jinja2.FileSystemLoader(searchpath='templates/')
    templateEnv = jinja2.Environment(loader=templateLoader)
    # add markdown filter
    templateEnv.filters['markdown'] = markdown
    templateEnv.filters['markdownrp'] = markdownrp
    return {
        template.split('.', 1)[0] : templateEnv.get_template(template)
        for template in templateEnv.list_templates(filter_func=filterTemplates)
    }

def updateProjects(site, pages):
    for p in pages:
        if p not in site['order']:
            site['order'].insert(0, p)
    dumpYaml('site.yaml', site)
    return site

def reorder(projects, order):
    neworder = []
    for elem in order:
        for p in projects:
            if p['slug'] == elem:
                neworder.append(p)
    return neworder

def readPage(root, fn):
    page = {'data': {}, 'boxes': []}
    with open(os.path.join(root, fn), 'r') as f:
        rawContent = f.read().split('---')[1:]
    if len(rawContent) > 0:
        page['data'] = yaml.load(rawContent.pop(0))
        for block in rawContent:
            [_type, content] = block.split('\n', 1)
            if _type == 'box':
                page['boxes'].append(markdown(content))
            elif content != '':
                page['content' if _type is '' else _type] = markdown(content)
    return page

def getPages(config):
    pages = {lang: {'home': None, 'pages': []} for lang in config['langs']}
    common = None
    for root, dirs, files in os.walk(config['pages']):
        for dir in dirs:
            if dir in config['forbiddenFolders']:
                dirs.remove(dir)
        if 'common.yaml' in files:
            common = getYaml(os.path.join(root, 'common.yaml'))
        for file in files:
            if file.endswith('.md'):
                page = readPage(root, file)
                data = page['data']
                if common is not None:
                    page['data'] = {**common, **data}
                [page['data']['template'], page['data']['lang'], _] = file.split('.')
                page['data']['uri'] = root + '/'
                page['data']['slug'] = os.path.basename(root)
                if page['data']['template'] == 'home':
                    pages[page['data']['lang']]['home'] = page
                else:
                    pages[page['data']['lang']]['pages'].append(page)
                # create folders 'fr' and 'en' if they don't exist
                for lang in config['langs']:
                    os.makedirs(root + '/' + lang, exist_ok=True)
        common = None
    return pages

def generate(onlyHome, slug):
    templates = getTemplates()
    trad = getYaml('languages.yaml')
    site = getYaml('site.yaml')
    pages = getPages(site)
    site = updateProjects(site, [p['data']['slug'] for p in pages['fr']['pages'] if p['data']['template'] == 'project'])

    for lang, content in pages.items():
        site['footer'] = content['home']['footer']
        site['meta'] = content['home']['data']['meta']
        projects = []
        for page in content['pages']:
            data = page['data']
            if data['template'] == 'project':
                projects.append(data)
            if not data['visible'] or onlyHome or (slug is not None and slug != data['slug']):
                continue
            print('Rendering {}…'.format(os.path.join(data['uri'], lang)))
            templates[data['template']].stream(
                site=site,
                page=page,
                trad=trad[lang],
            ).dump('{}/{}/index.html'.format(data['uri'], data['lang']))

        print('Rendering {}…'.format(os.path.join(site['pages'], lang)))
        templates['home'].stream(
            site=site,
            page=content['home'],
            projects=reorder(projects, site['order']),
            trad=trad[lang],
        ).dump('{}{}/index.html'.format(content['home']['data']['uri'], lang))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='landpagev2')
    parser.add_argument('--home', action='store_true')
    parser.add_argument('--slug', help='slug of project')
    parser = parser.parse_args()
    generate(parser.home, parser.slug)
