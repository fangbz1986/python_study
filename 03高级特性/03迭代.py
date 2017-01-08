#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    迭代
        给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
        python中，迭代是通过for...in来完成的,dict也可以使用for in迭代

'''

#迭代list
a=[1,2,3,4]
for num in a:
    print(num)

#迭代tuple
a=('a','b','c','d')
for num in a:
    print(num)

#迭代dict的key
d={"a":1,"b":2,"c":3}
for key in d:
    print(key)

# 迭代dict的value
d = {"a": "aa", "b": "bb", "c": "cc"}
for value in d.values():
    print(value)

#单独迭代dict的key-value
d={"a":11,"b":22,"c":33}
for key in d:
    print(d[key])


#同时迭代key和value
d={"a":11,"b":22,"c":33}
for key,value in d.items():
    print(key,"=",value)

# 字符串也是一个可迭代对象
a="hello"
for str in a:
    print(str)

# 当使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不用太关心该对象究竟是list还是其他类型
# 如何判断一个对象是可迭代对象呢，方法是通过collections模块的Iterable类型判断

from collections import Iterable

flag = isinstance("abc",Iterable)
print(flag)# true

flag = isinstance([1,2,3],Iterable)
print(flag)# true

flag = isinstance(123,Iterable)
print(flag)# true

# 最后一个问题，如果真的需要在迭代过程中使用下标，可以使用python内置的enumerate函数，可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

a=[1,2,3,4]
for i,value in enumerate(a):
    print(i,value)