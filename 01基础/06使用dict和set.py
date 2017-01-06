#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

    和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。

    dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

    这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

    要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

'''

# 初始化字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
print (d['Michael']);

# 修改值
d['Michael']=100;
print (d['Michael']);

# key 不存在会报错
# d['Thomas']

#避免key不存在的错误，有两种方式

# 使用in判断key是否存在
print ('Thomas' in d);

#使用dict提供的get方法，如果key不存在，则返回None，或者指定默认值
print(d.get('Thomas'));
print(d.get('Thomas', -1));

# 删除一个key
d.pop("Bob");
print(d);


'''
    set和dict类似，是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
    set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

'''

# set的初始化
s = set([1, 2, 3])
print(s);

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s);

# 添加和删除元素
s.add(4)
s.remove(4)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

# 2, 3
print(s1 & s2);
# 1, 2, 3, 4
print (s1 | s2)

# 尝试把set放入 set 会报错 TypeError: unhashable type: 'list'
a = ['c', 'b', 'a', 'a', 'a']
# s3 = set([a])
# print (s3)


'''
    再议不可变对象
    list是可变对象
    str是不可变对象

'''

a = ['c', 'b', 'a']
a.sort();
print(a);

a = 'abc'
b =a.replace('a', 'A')
print(b)
print(a)


s=(1, 2, 3);
s2 = set([s])
print(s2)


