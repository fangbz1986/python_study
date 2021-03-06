#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

'''


# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

a = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(type(a)) # filter
print(list(a)) # filter


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

a = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(a)


'''
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
'''


