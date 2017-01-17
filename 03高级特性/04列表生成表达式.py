#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
'''

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
a = list(range(1,11))
print(a)

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L=[]
for x in range(1,11):
    L.append(x*x)

print(L)

# 方法一太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
L=[x * x for x in(range(1,11))]
print(L)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环外面还可以加if判断，这样我们就可以筛选出来仅偶数的平方
L=[x * x for x in range(1, 11) if x % 2 == 0]
print(L)#[4, 16, 36, 64, 100]


# 还可以使用两层循环，可以生成全排列
L=[m + n for m in 'ABC' for n in 'XYZ']
print(L) #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
L=[d for d in os.listdir('.')] #os.listdir可以列出文件和目录
print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,"=",v)

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k + '=' + v for k, v in d.items()]
print(L)

# 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
L=[s.lower() for s in L]
print(L)

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World', 'IBM', 'Apple']
L = [ x.lower() for L in isinstance(x,str) is True]
print(L)