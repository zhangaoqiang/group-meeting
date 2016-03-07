#encoding=utf-8
'''
Created on 2016年3月6日

@author: xuxiao
'''
'''
        装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
        装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
        概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
        其实就是包装类，实现为函数添加功能的作用。
'''
def bread(func) :
    def wrapper() :
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper
 
def ingredients(func) :
    def wrapper() :
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper
 
def sandwich(food="--sandwich--") :
    print food
 
sandwich()
#输出 : --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs :
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
@bread
@ingredients
def helloword(keyword="--helloword--") :
    print keyword
helloword()
#输出 :
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
#######应用实例##############
'''
@ensure_csrf_cookie
@cache_if_anonymous()
def index(request):
'''