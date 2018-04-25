from jinja2 import Environment, FileSystemLoader, select_autoescape

import json

from os import path

# __version__ = '0.0.0'
# __version_full__ = __version__


def get_cur_dir():
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir

env = Environment(
    loader=FileSystemLoader('./templates/'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')

def get_context_from_json():
    with open('./uploads/test1.json', 'r') as f:
        global json_data
        json_data = json.loads(f.read())
    return json_data

task_list = {
    'blog_posts': {
        'singular': 'post_single.html',
        'others': ['blog_index.html','features.html']
        },
    'events': {
        'singular': 'event_single.html',
        'others': ['events.html']
        },
    'authors': {
        'singular': 'none',
        'others': ['none']
        }
}


# profile the uploads directory
# compare contents with build_history (last record)
# parse new/updated json to look for errors before starting build

# have jinja process each template in the list
# write new html files to site dir
# process/validate images and copy to static dir

# commands/modes:

# execute on repo update
# - if these dirs have changes: static, templates, config.py, then rebuild the whole site (stop)
# - if uploads dir has changes, then parse json, then process templates specified in task list







if __name__ == '__main__':
    get_context_from_json()
    for key, value in json_data:
        print(key + ": " + value)
    # print(template.render(d=json_data))
