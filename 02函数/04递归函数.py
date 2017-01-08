#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

    举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：

    fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

    所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。

    于是，fact(n)用递归的方式写出来就是：

'''

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)




'''
   如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
    ===> fact(5)
    ===> 5 * fact(4)
    ===> 5 * (4 * fact(3))
    ===> 5 * (4 * (3 * fact(2)))
    ===> 5 * (4 * (3 * (2 * fact(1))))
    ===> 5 * (4 * (3 * (2 * 1)))
    ===> 5 * (4 * (3 * 2))
    ===> 5 * (4 * 6)
    ===> 5 * 24
    ===> 120

'''
a = fact(1)
print(a)
a = fact(5)
print(a)

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# a = fact(10000)


# 尾递归调用

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

a = fact_iter(1,120)
print(a)



# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')