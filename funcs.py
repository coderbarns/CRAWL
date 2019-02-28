import os


def set_to_file(links, path):
    delete_file_contents(path)
    for link in sorted(links):
        append_to_file(path, link)


def file_to_set(path):
    new_set = set()
    with open(path, 'rt') as file:
        for line in file:
            new_set.add(line.replace('\n', ''))
    return new_set


def create_site_dir(config):
    d = config['project_dir']
    if not os.path.exists(d):
        print('Creating directory: ' + d)
        os.makedirs(d)
    else:
        print(config['project'] + " already exists in " + config['parent'])


def write_file(path, base_url):
    f = open(path, 'w')
    f.write(base_url)
    f.close()


def append_to_file(path, url):
    with open(path, 'a') as file:
        file.write(url + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


def create_file(path, url):
    if not os.path.isfile(path):
        write_file(path, url)


def create_site_files(config):
    create_file(config['queue'], config['base_url'])
    create_file(config['crawled'], '')
