# encoding=utf-8
'''
Created on 2016年3月6日

@author: xuxiao
'''
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。
function1 = lambda x, y, z:x + y + x

print function1(1, 2, 3)

function1 = lambda x, y, z:x + y + z

print function1(1, 2, 3)
##########################
# python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合
# （链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，
# 得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
######实现1*2*3*4*5的计算
n = 5
# range(1,5) #代表从1到5(不包含5)[1, 2, 3, 4，5]
print reduce(lambda x, y:x * y, range(1, n + 1))
# 120
##################应用实现排序############
L = [('b',2),('a',1),('c',3),('d',4)]
print sorted(L, key=lambda x:x[1])
#[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

'''
key=lambda course: (course.has_ended(), course.start is None, course.start),
    courses = sorted(
        courses,
        key=lambda course: (course.has_ended(), course.start is None, course.start),
        reverse=False
    )
'''