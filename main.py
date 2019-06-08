import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import sys
import argparse

import keylogger
import gui


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cli', action='store_true')
    return parser.parse_args(sys.argv[1:])

def main():
    args = parse_args()
    if args.cli:
        kl = keylogger.Keylogger()
        kl.listen()
    else:
        app = gui.QApplication(sys.argv)
        mw = gui.MainWindow()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()
