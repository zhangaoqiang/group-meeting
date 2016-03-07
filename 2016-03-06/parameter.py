#encoding=utf-8
'''
Created on 2016年3月6日

@author: xuxiao
'''
'''
Python中函数的参数有4种形式，分别是：
位置或关键字参数(Positional-or-keyword parameter)
仅位置的参数(Positional-only parameter)
任意数量的位置参数(var-positional parameter)
任意数量的关键字参数(var-keyword parameter)
'''
##############第一种：位置或关键字参数###############
'''
这种参数是Python中默认的参数类型，定义这种参数后，可以通过位置参数，或者关键字参数的形式传递参数：
'''
## 位置或者关键字参数
## 这个是Python的默认参数类型
## 示例：arg2提供了默认value
def func(arg1,arg2="World"):
    print arg1,arg2
## func可以通过位置参数形式调用
func("Hello", "MitchellChu")
## 也可以通过关键字参数的形式来调用func
func(arg1="Hello", arg2="World!")
## 当然，混合的方式也是完全没有问题的
func("Hello", arg2="World!")
################## 第二种方式：仅适用位置参数的形式###############
'''
 第二种方式：仅适用位置参数的形式
这种形式在需要将参数传递给函数(方法)时，仅能通过位置参数的传递方式。这种形式对于Python的开发者来说，暂时并没有办法使用。这种形式现在仅存在Python的很多内建的函数上：
'''
## Positional-only parameter has no syntax to define
## 虽然无定义方法，但内建的很多函数都是仅接受位置参数的
#abs(-3) ## correct
#abs(a=-3) ## wrong
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## TypeError: abs() takes no keyword arguments
#pow(x=2,y=3)
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## TypeError: pow() takes no keyword arguments
#pow(2,3)
## 8
################第三种：任意数量的位置参数（带单个星号参数）#################333
'''
任意数量的位置参数在定义的时候是需要一个星号前缀来表示，在传递参数的时候，可以在原有参数的后面添加任意多个参数，这些参数将会被放在元组内提供给函数(方法)：
'''
## var-positional parameter
## 定义的时候，我们需要添加单个星号作为前缀
def func3(arg1, arg2, *args):
    print arg1, arg2, args
 
## 调用的时候，前面两个必须在前面
## 前两个参数是位置或关键字参数的形式
## 所以你可以使用这种参数的任一合法的传递方法
func3("hello", "Tuple, values is:", 2, 3, 3, 4)
 
## Output:
## hello Tuple, values is: (2, 3, 3, 4)
## 多余的参数将自动被放入元组中提供给函数使用
 
## 如果你需要传递元组给函数
## 你需要在传递的过程中添加*号
## 请看下面例子中的输出差异：
 
func3("hello", "Tuple, values is:", (2, 3, 3, 4))
 
## Output:
## hello Tuple, values is: ((2, 3, 3, 4),)
 
func3("hello", "Tuple, values is:", *(2, 3, 3, 4))
 
## Output:
## hello Tuple, values is: (2, 3, 3, 4)
###########第四种：任意数量的关键字参数（带两个星号参数）###############
'''
任意数量的关键字参数在定义的时候，参数名称前面需要有两个星号(**)作为前缀，
这样定义出来的参数，在传递参数的时候，可以在原有的参数后面添加任意多个关键字参数，
关键字参数是使用[参数名称=参数值]的形式进行传递：
'''
## var-keywords parameter
## 定义的时候，需要两个星号作为前缀
def func4(arg1, arg2, **kwargs):
    print arg1, arg2, kwargs
 
func4("hello1", "Dict, values is:", x=2, y=3, z=3)
 
## Output:
## 多余的参数将自动被放入字典中提供给函数使用
 
## 如果你需要直接传递字典给函数
## 你需要在传递的过程中添加**
## 此时如果还有关键字参数应在字典前提供完成
## 不能在字典后再提供
## 请看下面例子中的输出差异：
 
func4("hello2", "Dict., values is:", **{'x':2, 'y':3, 'z':3})
## hello Dict., values is: {'y': 3, 'x': 2, 'z': 3}
 
 
#func4("hello3", "Dict., values is:", {'x':2, 'y':3, 'z':3})
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## TypeError: func() takes exactly 2 arguments (3 given)
 
func4("hello4", "Dict., values is:", s=3, **{'x':2, 'y':3, 'z':3,})
## hello Dict., values is: {'y': 3, 'x': 2, 's': 3, 'z': 3}
 
## 提供了重复的参数
#func4("hello5", "Dict., values is:", y=3, **{'x':2, 'y':3, 'z':3,})
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## TypeError: func() got multiple values for keyword argument 'y'
