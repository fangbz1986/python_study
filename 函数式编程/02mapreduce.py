#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

Python内建了map()和reduce()函数。


我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


'''


def f(x):
    return x*x

result =  map(f,[1,2,3,4,5,6,7,8,9])
print(type(result)) # map ?
result=list(result)
print(result)


L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)


'''
你可能会想，不需要map()函数，写一个循环，也可以计算出结果：
的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
'''

a = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(a))


'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

from functools import reduce
def add(x, y):
    return x+y

a =  reduce(add,[1,2,3,4,5])
print(a)


'''
当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

'''

def fn(x, y):
    return x*10+y


a =  reduce(fn, [1, 3, 5, 7, 9])
print(a) #13579


# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

def fn(x, y):
    return x*10+y

def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

s = reduce(fn, map(char2num, '13579'))
print(s) #13579

# 整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

num =  str2int('1')
print(num)


# 还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))



# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    if not isinstance(name, str):
        raise TypeError('bad operand type')

    if not name:
        return name
    head = name[0].upper()
    if len(name) == 1:
        return head
    return head + name[1:].lower()

L1 = ['adam', 'LISA', 'barT', '', 'a']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def str2num(numstr):
        return reduce(lambda x, y: x * 10 + y, map(lambda x: ord(x) - ord('0'), numstr))

    s = s.split('.')

    iii = str2num(s[0])
    if len(s) == 1:
        return float(iii)
    return iii + str2num(s[1]) / 10 ** len(s[1])

ret = str2float('1234.56789')
print(ret, type(ret))