#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    生成器

    通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

    所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

    要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

    创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
'''

# 列表生成式
L = [x * x for x in range(10)]
print(L)

# 生成器 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 使用next()有点变态，正确的方法是使用for循环，因为generator也是可迭代对象
g = (x * x for x in range(10))
for n in g:
    print(n)


'''
    著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
    a, b = b, a + b
    t = (b, a + b) # t是一个tuple
    a = t[0]
    b = t[1]
    但不必显式写出临时变量t就可以赋值。
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib(10)
print(f)

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：
# odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)
# next(o)


'''
 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
'''

for n in fib(6):
    print(n)

'''
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''
g = fib(6)

while True:
    try:
        x=next(g)
        print("g:",x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''
总结

generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

'''
