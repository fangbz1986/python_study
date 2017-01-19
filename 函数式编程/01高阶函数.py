#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

高阶函数
高阶函数英文叫Higher-order function。什么是高阶函数？我们以实际代码为例子，一步一步深入概念。

一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
编写高阶函数，就是让函数的参数能够接收别的函数。
函数式编程就是指这种高度抽象的编程范式



'''


'''
    变量可以指向函数
    以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码
    但是，如果只写abs呢？可见，abs(-10)是函数调用，而abs是函数本身。
    如果把函数本身赋值给变量呢？
    结论：函数本身也可以赋值给变量，即：变量可以指向函数;函数名也是变量
'''
a=abs(-10)
print(a)

print(abs) # <built-in function abs>

# 如果把函数本身赋值给变量呢？
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数
f = abs
print(f) # <built-in function abs>
print(f(-10)) # <built-in function abs>


'''
    传入函数
    既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
'''

'''
    一个简单的高阶函数
    当我们调用 add(-5,6,abs)时，参数x,y和f分别接受 -5,6和abs，我们可以推导计算过程为：
    x = -5
    y = 6
    f = abs
    f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
    return 11
'''

def add(x,y,f):
    return f(x)+f(y)

a = add(-6,5,abs)
print(a)
