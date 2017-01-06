#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
   根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

   也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了

'''

# if
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


# if else
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# if elseif else
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if 判断还可以简写
if True:
    print('True')

# input接受的字符串，可以使用int进行转换
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')