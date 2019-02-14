from funcs import *
from parser import LinkFinder
from urllib.request import urlopen

class Spider:

    project_name = ''
    project_dir = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, config):
        self.config = config
        Spider.project_name = self.config['project']
        Spider.base_url = self.config['base_url']
        Spider.domain_name = self.config['domain_name']
        Spider.queue_file = self.config['queue']
        Spider.crawled_file = config['crawled']
        self.boot()
        self.crawl_page('Spider one', Spider.base_url)

    @staticmethod
    def boot(self):
        create_site_dir(config['parent'], self.config['project_dir'])
        create_site_files()
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

with open('config.json', 'r') as f:
    config = json.load(f)
