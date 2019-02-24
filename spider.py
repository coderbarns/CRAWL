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
    def boot():
        create_site_dir(config['parent'], self.config['project_dir'])
        create_site_files()
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    def crawl_page(self, thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.queue.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(config['base_url'], page_url)
            finder.feed(html_string)

        except:
            print("Error: Can't crawl the page :/")
            return set()

        return(finder.page_links())

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)

with open('config.json', 'r') as f:
    config = json.load(f)


