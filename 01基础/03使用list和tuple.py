#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    list
        list是可变的有序列表，可以随时添加和删除其中的元素,list中的元素类型是不固定的
        可以通过索引访问，默认从0开始，也支持负数，例如-1表示最好一个元素
        append()方法添加元素到末尾
        pop()方法删除末尾元素
'''

# list的初始化
classmates =["zhangsan","lisi","wuwang"];
print (classmates);

# list的长度
print (len(classmates));

# 通过索引访问list的元素,索引从0开始
print (classmates[0]);
print (classmates[1]);

# 当超出索引范围的时候，会提示 IndexError: list index out of range
# print (classmates[10])

# 使用负数索引，支持倒序取
print (classmates[-1]);
print (classmates[-2]);

# 追加元素到末尾
classmates.append('Adam')
print (classmates);

# 要删除list末尾的元素
classmates.pop();
print (classmates);

# 替换指定元素
classmates[1]="fangbz"
print (classmates);

# 支持二维，三维等多维
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))


p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']


'''
    tuple
    另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
    获取元素的方式和list完全一致

    tuple有一个陷阱，就是在定义一个tuple的的时候，元素必须确定下来

'''

classmates = ('Michael', 'Bob', 'Tracy')

print (len(classmates));
print(classmates[0]);
print(classmates[-1]);


# 不能变
# classmates[0]="fangbz";

# tuple 初始化陷阱
t=(1,2);
print(t);

# 定义一个空的 tuple
t=();
print(t);

# 但是要定义一个只有1个元素的tuple，这样定义的不是tuple，而是1这个数
# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这样就产生了歧义
# 因此，python规定这种情况下，按小括号进行计算，计算结果自然是1
t=(1);
print(t);

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t=(1,);
print(t);


# "可变的" tuple，实际上变的不是tuple的元素而是list的元素
# tuple所谓的"不变"是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
print(t);
t[2][0] = 'X';
t[2][1] = 'Y';
print(t);