from funcs import *
from parser import LinkFinder
from urllib.request import urlopen, Request
from domain import get_domain


class Spider:

    project_name = ''
    project_dir = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    config = dict()

    def __init__(self, cfg):
        Spider.config = cfg
        Spider.project_name = Spider.config['project']
        Spider.base_url = Spider.config['base_url']
        Spider.domain_name = get_domain(Spider.base_url)
        Spider.queue_file = Spider.config['queue']
        Spider.crawled_file = Spider.config['crawled']
        self.boot()
        self.crawl_page('Spider one', Spider.base_url)

    @staticmethod
    def boot():
        create_site_dir(Spider.config)
        create_site_files(Spider.config)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            req = Request(page_url)
            print("HI")
            response = urlopen(req)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.config['base_url'], page_url)
            finder.feed(html_string)

        except Exception as e:
            print("Error: Can't crawl the page  :/")
            print(e)
            return set()

        return finder.page_links()

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
