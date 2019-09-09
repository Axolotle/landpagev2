import os
import jinja2
from markdown import markdown
from ruamel.yaml import YAML

yaml=YAML(typ='safe')

def getYaml(path):
    with open(path) as f:
        return yaml.load(f)

def getTemplates():
    def filterTemplates(fn):
        if 'partials/' not in fn:
            return True

    templateLoader = jinja2.FileSystemLoader(searchpath='templates/')
    templateEnv = jinja2.Environment(loader=templateLoader)
    return {
        template.split('.', 1)[0] + '.md': templateEnv.get_template(template)
        for template in templateEnv.list_templates(filter_func=filterTemplates)
    }

def readPage(root, fn):
    page = {'data': {}}
    with open(os.path.join(root, fn), 'r') as f:
        rawContent = f.read().split('---')[1:]
    if len(rawContent) > 0:
        page['data'] = yaml.load(rawContent.pop(0))
        for block in rawContent:
            [_type, content] = block.split('\n', 1)
            if content != '':
                page['content' if _type is '' else _type] = markdown(content)
    page['data']['uri'] = '/' + os.path.dirname(root) + '/'
    page['data']['lang'] = os.path.basename(root)
    return page

def main():
    templates = getTemplates()
    site = getYaml('site.yaml')
    projects = {lang: [] for lang in site['langs']}
    for root, dirs, files in os.walk('landpage'):
        for fn in files:
            if fn.endswith('.md') and fn != 'home.md':
                page = readPage(root, fn)
                if page:
                    print('Rendering {}/{}…'.format(root, fn))
                    templates[fn].stream(site=site, page=page).dump(os.path.join(root, 'index.html'))
                    if fn == 'project.md':
                        projects[page['data']['lang']].append(page['data'])

    for lang, list in projects.items():
        print('Rendering landpage/{}/home.md…'.format(lang))
        page = readPage('landpage/'+lang, 'home.md')
        templates['home.md'].stream(site=site, page=page, projects=list).dump('landpage/{}/index.html'.format(lang))

if __name__ == '__main__':
    main()
