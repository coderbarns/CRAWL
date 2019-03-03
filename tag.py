from urllib import parse

class TagHandler():

    def __init__(self, config, parser):
        self.parser = parser
        self.config = config
        self.func_dict = dict()
        self.initialize_func_dict()

    def initialize_func_dict(self):
        method_list = [func for func in dir(Language) if callable(getattr(Language, func)) and not func.startswith("__")]
        for func in method_list:
            tag = func.split("_")[0]
            self.func_dict[tag] = func

    def tag_handler(self, tag, attrs):
        try:
            func = self.func_dict[tag]
            string = "self.{}({})".format(func, attrs)
            exec(string)
        except:
            pass

    def a_handler(self, attrs):
        for (attr, value) in attrs:
            if attr == 'href':
                url = parse.urljoin(self.parser.base_url, value)
                self.parser.currently_parsing = url
                self.parser.links.add(url)

    def div_handler(self, attrs):
        for (attr, value) in attrs:
            print(attr)


lang = Language("")
lang.tag_handler('a', [('href', 'link')])
