import threading
import mkconfig
from queue import Queue
from spider import Spider
from funcs import *
import sys
import json


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(config['threads']):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(config['queue']):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(config['queue'])
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


if len(sys.argv) > 2:
    print("Too many arguments: Exiting.")
    sys.exit()

if len(sys.argv) > 1:
    config_file = sys.argv[1]
else:
    config_file = 'config.json.example'
    mkconfig.make()

with open(config_file, 'r') as f:
    config = json.load(f)

queue = Queue()
Spider(config)
create_workers()
crawl()
