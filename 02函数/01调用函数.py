#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
    python自带很多函数
    调用函数的时候，传入的参数不对或者类型不对，会报TypeError错误
    函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
    a = abs
    a(-1)
'''

# 调用abs函数

a = abs(100)
print (a)
a = abs(-100)
print (a)

# max函数 min函数
a = max(1,2,4,5,7)
print (a)
a = min(1,2,4,5,7)
print (a)

# 数据类型转换函数
a = int('123')
print (a)

a = int(12.2)
print (a)

a = str(1.23)
print (a)

a = bool(1)
print (a)




# 调用函数的时候，传入的参数不对或者类型不对，会报TypeError错误
# abs(1, 2)
# abs("a")

