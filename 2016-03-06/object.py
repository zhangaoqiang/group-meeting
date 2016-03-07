# encoding=utf-8
'''
Created on 2016年3月6日

@author: xuxiao
'''
class Employee:
    '''所有员工的基类'''
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print"Total Employee %d"%Employee.empCount
    def displayEmployee(self):
        print"Name : ",self.name,", Salary: ",self.salary
#empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
#第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法        

emp1 =Employee("Zara",2000)#"创建 Employee 类的第二个对象"
emp2 =Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print"Total Employee %d"%Employee.empCount

emp1.age =7# 添加一个 'age' 属性
emp1.age =8# 修改 'age' 属性del emp1.age  # 删除 'age' 属性
'''
你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
'''
print hasattr(emp1,'age')# 如果存在 'age' 属性返回 True。
getattr(emp1,'age')# 返回 'age' 属性的值
setattr(emp1,'age',8)# 添加属性 'age' 值为 8
#delattr(emp1,'age')# 删除属性 'age'
######################内置类属性################
'''
Python内置类属性

__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
Python内置类属性调用实例如下：
'''
print"Employee.__doc__:",Employee.__doc__
print"Employee.__name__:",Employee.__name__
print"Employee.__module__:",Employee.__module__
print"Employee.__bases__:",Employee.__bases__
print"Employee.__dict__:",Employee.__dict__
#############类的继承############
'''
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
在python中继承中的一些特点：
1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
语法：
派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
classSubClassName(ParentClass1[,ParentClass2,...]):'Optional class documentation string'
   class_suite
'''
class Parent:#定义父类
    parentAttr =100
    def __init__(self):
        print"调用父类的构造函数"
    def parentMethod(self):
        print"调用父类方法 parentMethod"
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print "父类属性：",Parent.parentAttr
class Child(Parent):#定义子类
    def __init__(self):
        print "调用子类构造方法"
    def childMethod(self):
        print'调用子类方法child method'
    #def parentMethod(self):
        #print"子类方法重写parentMethod"
c=Child()# 实例化子类
c.childMethod()# 调用子类的方法
c.parentMethod()# 调用父类方法
c.setAttr(200)# 再次调用父类的方法
c.getAttr()# 再次调用父类的方法
'''
调用子类构造方法调用子类方法 child method
调用父类方法父类属性:200
'''
'''
class A:# 定义类 A.....class B:# 定义类 B.....class C(A, B):# 继承类 A 和 B.....
你可以使用issubclass()或者isinstance()方法来检测。
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
'''
##############方法重写################
'''
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
实例：
'''
#####################类属性与方法##################
'''
类的私有属性

__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法

在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数

类的私有方法

__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
'''
class JustCounter:
    __secretCount =0#私有变量
    publicCount =0# 公开变量
    def count(self):
        self.__secretCount+=1
        self.publicCount +=1
        print self.__secretCount
    
counter =JustCounter()
counter.count()
counter.count()
print "publicCount",counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的最后一行代码：
print counter._JustCounter__secretCount
