import logging
logger = logging.getLogger(__name__)

import getkey as gk

# class Keylogger(object):
#
#     def __init__(self):
#         super().__init__()
#         platform = gk.platform(interrupts={})
#         self.getkey = platform.getkey
#
#     def listen(self):
#         while True:
#             key = self.getkey()
#             logging.debug([key, gk.keys.canon(key), gk.keys.name(key),
#                            gk.keys.code(key)])
#
#             if gk.keys.name(key) == 'ESC':
#                 break


from pynput.keyboard import Key, Listener

class Keylogger(object):

    def __init__(self):
        super().__init__()

    def listen(self):
        with Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.run()
            # pass

    def on_press(self, key):
        logging.debug(key)

    def on_release(self, key):
        if key == Key.esc:
            return False
