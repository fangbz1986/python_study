#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

    python函数的参数

    python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

    默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

    要注意定义可变参数和关键字参数的语法：

    *args是可变参数，args接收的是一个tuple；

    **kw是关键字参数，kw接收的是一个dict。

    以及调用函数时如何传入可变参数和关键字参数的语法：

    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

    定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

'''


# 位置参数,当我们调用power函数时，必须传入有且仅有一个参数
def power(x):
    return x*x

# 如果要计算三次方怎么办
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 默认参数
# 默认参数的特点 1.必选参数在前，默认参数在后  2.默认参数的好处降低函数的难度
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name,gender):
    print ("name:",name)
    print ("gender:",gender)

enroll("xiaofang","man")

# 如果要继续传入年龄，城市等信息怎么办，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

# 默认函数的坑，先定义一个函数，传入一个list，添加一个END再返回：
# 出现下面最终原因的解释如下
# python函数在定义的时候，默认参数L的值会被计算出来，即[]，默认参数L也是一个变量，它指向[],每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所以，定义默认参数，要牢记一点：默认参数必须指向不可变对象来实现
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误，此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读
# 一点问题都没有
def add_end(L=[]):
    L.append('END')
    return L

a =  add_end([1, 2, 3]);
print (a) # 结果正确
a =  add_end(['x','y','z']);
print (a) # 结果正确

a =  add_end();
print (a) # 结果正确 ['END']
a = add_end()
print (a) # 结果不正确  ['END', 'END']

# 默认参数指向不可变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print (add_end())
print (add_end())


# 可变参数，顾名思义，可变参数就是传入的参数个数是可变的，可以是1个，2个到任意个，还可以是0个，这些可变参数在函数调用时，自动组装成一个tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用的时候，需要先组装一个list或tuple，也可以直接写
a = calc([1, 2, 3])
print (a)
a = calc((1, 3, 5, 7))
print (a)
#直接简化传参数就不行了
#a = calc(1, 3, 5, 7)
#print (a)

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部numbers接收到一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用函数的时候，可以传递进任意参数
a = calc(1, 3, 5, 7)
print (a)
a = calc()
print (a)

# 如果已经有一个list或者tuple怎么办
nums=[1,2,3]
num=(1,2,3)
a = calc(nums[0],nums[1],nums[2])
print (a)

# 上面的方法虽然是可行的，但是太麻烦. *nums表示把nums这个list的所有元素作为可变参数传进去，这种写法相当有用而且常见
a = calc(*nums)
print (a)

a = calc(*num)
print (a)

# 关键字参数
# 可变参数允许传入0个或任意个参数，这些可变参数在函数调用时，自动组装成一个tuple
# 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组成一个dict
# 关键字参数有什么用，它可以扩展函数的功能，比如person函数里面，我们保证能接收到name和age两个参数，但是如果调用者愿意提供更多参数，我们也能收到
# 试想你正在做一个用户注册功能，除了用户名和年龄必填外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求

# 示例
def person(name,age,**kw):
    print ('name=',name,'age=',age,'others=',kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装一个dict，然后把dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 简化写法
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 24, **extra)


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了哪些，就需要在函数内部通过kw来检查
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 调用者仍可以传入不受限制的关键字参数：
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如city和job作为关键字参数，定义方式如下
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错,由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数
# person('Jack', 24, 'Beijing', 'Engineer')


# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
person('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 比如定义一个函数，包含上述若干种参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去

f1(1, 2) # a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3) #a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b') #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None) #a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 最神奇的是通过一个tuple和dict，你也可以用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) #a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}