#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: weiyunfei  date: 2017-05-21

import ctypes
from sys import stdout

GetStdHandle = ctypes.windll.kernel32.GetStdHandle
GetConsoleScreenBufferInfo = ctypes.windll.kernel32.GetConsoleScreenBufferInfo
SetConsoleTextAttribute = ctypes.windll.kernel32.SetConsoleTextAttribute

stdoutHandle = -11


def getOldColor():
    class Coord(ctypes.Structure):
        _fields_ = [('X', ctypes.c_short),
                    ('Y', ctypes.c_short),
                    ]

    class SmallRect(ctypes.Structure):
        _fields_ = [('Left', ctypes.c_short),
                    ('Top', ctypes.c_short),
                    ('Right', ctypes.c_short),
                    ('Bottom', ctypes.c_short),
                    ]

    class ConsoleScreenBufferInfo(ctypes.Structure):
        _fields_ = [('dwSize', Coord),
                    ('dwCursorPosition', Coord),
                    ('wAttributes', ctypes.c_uint),
                    ('srWindow', SmallRect),
                    ('dwMaximumWindowSize', Coord),
                    ]

    cmdInfo = ConsoleScreenBufferInfo()
    GetConsoleScreenBufferInfo(
        GetStdHandle(stdoutHandle),
        ctypes.byref(cmdInfo))
    return cmdInfo.wAttributes

COLORS = {
    'black'     : 0x00,     'gray'          : 0x08,
    'blue'      : 0x01,     'lightblue'     : 0x09,
    'green'     : 0x02,     'lightgreen'    : 0x0a,
    'cyan'      : 0x03,     'lightcyan'     : 0x0b,
    'red'       : 0x04,     'lightred'      : 0x0c,
    'magenta'   : 0x05,     'lightmagenta'  : 0x0d,
    'yellow'    : 0x06,     'lightyellow'   : 0x0e,
    'white'     : 0x07,     'lightwhite'    : 0x0f,
}

BGCOLORS = {
    'black'     : 0x00,     'gray'          : 0x80,
    'blue'      : 0x10,     'lightblue'     : 0x90,
    'green'     : 0x20,     'lightgreen'    : 0xa0,
    'cyan'      : 0x30,     'lightcyan'     : 0xb0,
    'red'       : 0x40,     'lightred'      : 0xc0,
    'magenta'   : 0x50,     'lightmagenta'  : 0xd0,
    'yellow'    : 0x60,     'lightyellow'   : 0xe0,
    'white'     : 0x70,     'lightwhite'    : 0xf0,
}

_oldColor = getOldColor()


class color(object):
    @staticmethod
    def black(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['black'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def blue(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['blue'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def green(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['green'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def cyan(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['cyan'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def red(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['red'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def magenta(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['magenta'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def yellow(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['yellow'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def white(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['white'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def gray(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['gray'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightblue(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightblue'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightgreen(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightgreen'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightcyan(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightcyan'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightred(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightred'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightmagenta(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightmagenta'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightyellow(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightyellow'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

    @staticmethod
    def lightwhite(msg, bgcolor=0, style=None):
        del style
        assert 0x00 <= bgcolor <= 0xff, '0x00 <= bgcolor <= 0xff'
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), COLORS['lightwhite'] + bgcolor)
        stdout.write(msg)
        stdout.flush()
        SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

def test():
    for ck,cv in COLORS.items():
        for bk,bv in BGCOLORS.items():
            SetConsoleTextAttribute(GetStdHandle(stdoutHandle), cv+bv)
            stdout.write('This is color test')
            stdout.flush()
            SetConsoleTextAttribute(GetStdHandle(stdoutHandle), _oldColor)

__all__ = ['getOldColor', 'test', 'color', 'COLORS', 'BGCOLORS']

if __name__ == "__main__":
    test()

