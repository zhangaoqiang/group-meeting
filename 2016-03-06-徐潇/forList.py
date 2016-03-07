#encoding=utf-8
'''
Created on 2016年3月6号

@author: xuxiao
'''
'''
列表解析

定义和说明

>Python 的强大特性之一是其对 list 的解析，它提供一种紧凑的方法，可以通过对 list 中的每个元素应用一个函数，从而将一个 list 映射为另一个 list。
>列表解析，又叫列表推导式( list comprehension)
>列表解析比 for 更精简，运行更快，特别是对于较大的数据集合
>列表解析可以替代绝大多数需要用到 map和 filter的场合
'''
#基本列表解析
#[x for x in range(5)]   # [0, 1, 2, 3, 4]
List1=range(5)#[0, 1, 2, 3, 4]
print List1
print [ x*2 for x in List1]
###########条件列表解析

print [ x for x in range(100) if x%2 ==0 ]
'''
courses = [c for c in courses if has_access(user, permission_name, c)]
'''
##########嵌套列表解析#############
mat = [ [1, 2, 3],[4, 5, 6], [7, 8, 9]]
#交换行列
print [ [row[i] for row in mat] for i in (0,1,2)] #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
