#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: weiyunfei  date: 2017-05-21

from sys import stdout

COLORS = {
    'black'     : 30,
    'red'       : 31,
    'green'     : 32,
    'yellow'    : 33,
    'blue'      : 34,
    'magenta'   : 35,
    'cyan'      : 36,
    'white'     : 37,
}

BGCOLORS = {
    'black'     : 40,
    'red'       : 41,
    'green'     : 42,
    'yellow'    : 43,
    'blue'      : 44,
    'magenta'   : 45,
    'cyan'      : 46,
    'white'     : 47,
}

STYLES = {
    'default'   : 0,
    'highlight' : 1,
    'underline' : 4,
    'blink'     : 5,
    'invert'    : 7,
    'hide'      : 8,
}

END = '\033[0m'

class color(object):
    @staticmethod
    def black(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
            filter(bool,[bgcolor,COLORS['black']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def red(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['red']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def green(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['green']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def yellow(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['yellow']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def blue(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['blue']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def magenta(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['magenta']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def cyan(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['cyan']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def white(msg,bgcolor=None,style=None):
        style = [] if style is None else style
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['white']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightblack(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['black']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightred(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['red']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightgreen(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['green']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightyellow(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['yellow']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightblue(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['blue']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightmagenta(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['magenta']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightcyan(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['cyan']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()

    @staticmethod
    def lightwhite(msg,bgcolor=None,style=None):
        style = [STYLES['highlight']] \
            if style is None else \
            style+[STYLES['highlight']]
        assert type(style) == type([]), "style's type should be list"
        code = ';'.join(map(str,
                            filter(bool,[bgcolor,COLORS['white']]+style)))
        stdout.write('\033[%sm'%code+msg+END)
        stdout.flush()


def test():
    for cv in COLORS.values():
        for bv in BGCOLORS.values():
            for sv in STYLES.values():
                stdout.write('\033[%s;%s;%smThis is color test' % (cv,bv,sv)+END)
                stdout.flush()


__all__ = ['END', 'test', 'color', 'COLORS', 'BGCOLORS', 'STYLES']

if __name__ == "__main__":
    test()
