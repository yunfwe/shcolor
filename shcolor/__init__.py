#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: weiyunfei  date: 2017-05-23

if __import__('platform').system() == 'Linux':
    from .linux import *
elif __import__('platform').system() == 'Windows':
    from .win32 import *