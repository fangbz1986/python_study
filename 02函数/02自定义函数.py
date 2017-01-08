#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

    python定义函数

    定义函数时，需要确定函数名和参数个数；

    如果有必要，可以先对参数的数据类型做检查；

    函数体内部可以用return随时返回函数结果；

    函数执行完毕也没有return语句时，自动return None。

    函数可以同时返回多个值，但其实就是一个tuple。

'''

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x



#print (my_abs(-1))

# 空函数,如果想定义一个什么事也不做的空函数，可以使用pass语句
# pass语句什么都不做，pass的实际作用是占位符，比如还没想好怎么写函数的代码，就可以先放一个pass，让代码运行起来
def nop():
    pass

# 参数检查
# 当调用python自带函数的时候，如果参数不正确，会抛出TypeError

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


   # a =  my_abs(10)
   # print(a)


# 返回多个值,但实际上返回多个值，只是一种假象

import math
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle);
    ny = y+step*math.cos(angle);
    return nx,ny

x, y = move(100, 100, 60, math.pi / 6)
print (x)
print (y)
# 返回多值，实际是一种假象，python函数返回的仍然是单一值,返回一个tuple可以省略括号，而多个变量可以同时接受一个tuple，按位置赋给对应的值，所以python的函数
x =  move(100, 100, 60, math.pi / 6)
print (x)
print ("end")