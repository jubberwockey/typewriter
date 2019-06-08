import json
import platform
import logging
logger = logging.getLogger(__name__)

class Typewriter(object):

    def __init__(self):
        super().__init__()
        # keypress tracking
        self.num_pressed = 0
        self.key_lst = []
        with open('./config/os_config.json', 'r') as os_config_file:
            os_config = json.load(os_config_file)
        self.modifiers = os_config[platform.system()]
        self.modifiers_inv = {v: k for k, v in self.modifiers.items()}

        with open('./config/translations.json', 'r') as t_file:
            self.translations = json.load(t_file)
        with open('./config/translations_modifiers.json') as tm_file:
            self.translations_modifiers = json.load(tm_file)
        with open('./config/mapping.json') as mapping_file:
            self.mapping = json.load(mapping_file)

        self.symbol_lst = [Symbol(r'\alpha')]
        self.symbol = r'{}'
        self.latex_str = ''


    def get_mapping(self, key_meta):
        modifier = self.translations_modifiers.get(key_meta['modifier'], None)
        # key_meta[id] is language specific... can this be circumvented?
        key = self.translations.get(key_meta['id'], None)

        # get mapping from mapping file if present, otherwise use default text
        if modifier in self.mapping:
            logging.debug("found modifer {}".format(modifier))
            modifier_mapping = self.mapping[modifier]
            map = modifier_mapping.get(key, key_meta['text'])
            logging.debug("found mapping {}".format(map))
            return map

    def process_key_pressed(self, key_meta):
        map_str = self.get_mapping(key_meta)
        self.latex_str += map_str
        logging.debug(self.latex_str)
        return self.latex_str

    def process_key_released(self):
        pass

    def parse_symbols(self):
        pass


class Symbol(object):

    def __init__(self, code):
        super().__init__()
        self.code = code
        self.up_left = []
        self.down_left = []
        self.up_right = []
        self.down_right = []

class Span(Symbol):

    def __init__(self, code):
        super().__init__(code)
        self.inner = []

class FracType(Symbol):

    def __init__(self, code=r'\frac'):
        super().__init__(code)
        self.up = []
        self.down = []

class Enclosure(Symbol):

    def __init__(self, code):
        super().__init__(code)
        self.inner = []

# matrices not supported by renderer
class Matrix(Symbol):

    def __init__(self, code):
        super().__init__(code)
