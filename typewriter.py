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

        self.symbol_lst = []
        self.symbol = r'{}'
        self.latex = r''
        self.mapping_old = {
'none': {
'32': r' ',
'39': r"'",
'44': r',',
'45': r'-',
'46': r'.',
'47': r'/',
'48': r'0',
'49': r'1',
'50': r'2',
'51': r'3',
'52': r'4',
'53': r'5',
'54': r'6',
'55': r'7',
'56': r'8',
'57': r'9',
'59': r';',
'61': r'=',
'65': r'a',
'66': r'b',
'67': r'c',
'68': r'd',
'69': r'e',
'70': r'f',
'71': r'g',
'72': r'h',
'73': r'i',
'74': r'j',
'75': r'k',
'76': r'l',
'77': r'm',
'78': r'n',
'79': r'o',
'80': r'p',
'81': r'q',
'82': r'r',
'83': r's',
'84': r't',
'85': r'u',
'86': r'v',
'87': r'w',
'88': r'x',
'89': r'y',
'90': r'z',
'91': r'[',
# '92': r'\\',
'93': r']',
# '96': r'`',
'167': r'§',
'16777217': r'\quad', # tab
'16777219': '', # backspace
'16777220': '', # enter
},
'16777251': {
'32': r' ',
'39': r"'",
'44': r',',
'45': r'-',
'46': r'.',
'47': r'/',
'48': r'0',
'49': r'1',
'50': r'2',
'51': r'3',
'52': r'4',
'53': r'5',
'54': r'6',
'55': r'7',
'56': r'8',
'57': r'9',
'59': r';',
'61': r'=',
'65': r'\alpha ',
'66': r'\beta ',
'67': r'\chi ',
'68': r'\delta ',
'69': r'\epsilon ',
'70': r'\phi ',
'71': r'\gamma ',
'72': r'\eta ',
'73': r'\iota ',
'74': r'j ',
'75': r'\kappa ',
'76': r'\lambda ',
'77': r'\mu ',
'78': r'\nu ',
'79': r'o ',
'80': r'\pi ',
'81': r'\theta ',
'82': r'\rho ',
'83': r'\sigma ',
'84': r'\tau ',
'85': r'\upsilon ',
'86': r'v ',
'87': r'\omega ',
'88': r'\xi ',
'89': r'y ',
'90': r'\zeta ',
'91': r'[',
# '92': r'\\',
'93': r']',
# '96': r'`',
'167': r'§',
'16777217': r'\quad', # tab
'16777219': '', # backspace
'16777220': '', # enter
}
}


    # def parse_settings(self, settings):


    def get_latex(self, key_lst):
        if int(key_lst[0]) <= 16777220: # no modifier
            modifier = 'none'
        else:
            modifier = key_lst[0]

        try:
            self.latex += self.mapping_old[modifier][key_lst[-1]]
        except:
            pass
        return self.latex

    def get_mapping(self, key_meta):
        pass

    def process_key_pressed(self, key_meta):
        self.modifier = self.translations_modifiers.get(key_meta['modifier'], None)
        # key_meta[id] is language specific... can this be circumvented?
        self.key = self.translations.get(key_meta['id'], None)

        # get latex mapping from mapping file if present, otherwise use default text
        if self.modifier in self.mapping:
            logging.debug("found modifer {}".format(self.modifier))
            modifier_mapping = self.mapping[self.modifier]
            self.latex_str = modifier_mapping.get(self.key, key_meta['text'])
            logging.debug("found mapping {}".format(self.latex_str))
            return self.latex_str

        key_str = str(key_meta['id'])
        if key_str != self.modifiers['meta']: # exclude win, mac cmd key
            self.num_pressed += 1
            self.key_lst.append(key_str)
            self.latex_str = self.get_latex(self.key_lst)
            # logging.debug("key_lst: {}, latex: {}".format(self.key_lst, self.latex_str))

    def process_key_released(self):
        if self.num_pressed > 0:
            self.num_pressed -= 1

        if self.num_pressed == 0:
            self.key_lst = []
