#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: weiyunfei  date: 2017-05-22

class utils(object):
    __doc__ = '''
    valueToKey(d, v)

        @argument d -> type(dict)
        @argument v -> type(str)
        @return key -> type(list)
        
        Find key from dict
    '''
    @staticmethod
    def valueToKey(d, v):
        index = 0
        result = []
        for _v in d.values():
            if _v == v:
                result.append(index)
            index += 1
        return [list(d.keys())[x] for x in result]

# data = {'a':1, 'b':2, 'c':1}
# print(utils.valueToKey(data,2))