import json

d = {}
d['parent'] = './Projects/'
d['project'] = 'projname'
d['project_dir'] = d['parent'] + d['project'] + '/'
d['base_url'] = 'https://www.projname.com/'
d['domain_name'] = '????'
d['queue'] = d['project_dir'] + 'queue.txt'
d['crawled'] = d['project_dir'] + 'crawled.txt'

with open('config.json.example', 'w') as f:
    json.dump(d, f)
