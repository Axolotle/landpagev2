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

def readPage(path):
    page = {}
    with open(path, 'r') as f:
        rawContent = f.read().split('---')[1:]
        if len(rawContent) > 0:
            page['data'] = yaml.load(rawContent.pop(0))
            for block in rawContent:
                [_type, content] = block.split('\n', 1)
                if content != '':
                    page['content' if _type is '' else _type] = markdown(content)
    return page

def main():
    templates = getTemplates()
    site = getYaml('site.yaml')
    for root, dirs, files in os.walk('pages'):
        for fn in files:
            if fn.endswith('.md'):
                page = readPage(os.path.join(root, fn))
                if page:
                    print('Rendering {}/{}…'.format(root, fn))
                    templates[fn].stream(site=site, page=page).dump(os.path.join(root, 'index.html'))


if __name__ == '__main__':
    main()
