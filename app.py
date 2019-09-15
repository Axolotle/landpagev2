import os
import jinja2
import re
from markdown import markdown as mdRenderer
from ruamel.yaml import YAML


yaml = YAML(typ='safe')


def markdown(text):
    p = re.compile('(!\[[^]]*]\()')
    return mdRenderer(p.sub(r'\1../medias/', text))

def getYaml(path):
    with open(path) as f:
        return yaml.load(f)

def getTemplates():
    def filterTemplates(fn):
        if 'partials/' not in fn:
            return True

    templateLoader = jinja2.FileSystemLoader(searchpath='templates/')
    templateEnv = jinja2.Environment(loader=templateLoader, extensions=['jinja2.ext.i18n'])
    # add markdown filter
    templateEnv.filters['markdown'] = markdown
    return {
        template.split('.', 1)[0] : templateEnv.get_template(template)
        for template in templateEnv.list_templates(filter_func=filterTemplates)
    }

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
                if page['data']['template'] == 'home':
                    pages[page['data']['lang']]['home'] = page
                else:
                    pages[page['data']['lang']]['pages'].append(page)
                # create folders 'fr' and 'en' if they don't exist
                for lang in config['langs']:
                    os.makedirs(root + '/' + lang, exist_ok=True)
        common = None
    return pages

def generate():
    templates = getTemplates()
    trad = getYaml('languages.yaml')
    site = getYaml('site.yaml')
    pages = getPages(site)

    for lang, content in pages.items():
        site['footer'] = content['home']['footer']
        site['meta'] = content['home']['data']['meta']
        projects = []
        for page in content['pages']:
            data = page['data']
            if data['template'] == 'project':
                projects.append(data)
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
            projects=projects,
            trad=trad[lang],
        ).dump('{}{}/index.html'.format(content['home']['data']['uri'], lang))


if __name__ == '__main__':
    generate()
