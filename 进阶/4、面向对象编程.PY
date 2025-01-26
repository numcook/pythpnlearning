#面向对象编程
#三个基本特征：封装、继承、多态
#封装：将数据和操作数据的方法放在一起，形成一个“类”，数据被保护在“类”内部，程序的其他部分只有通过被授权的方法才能访问数据   
#继承：一个类可以继承另一个类的属性和方法，从而实现代码的复用
#多态：一个类可以有多种表现形式，不同的对象可以调用相同的方法，但表现出来的行为却不同


#1）定义一个类

#class 类名(父类):
#    类体

#class Animal(object):
#    #类体
#    pass
#上述代码定义了一个Animal类，这个类继承自object类，object是所有类的基类，也叫根类
#pass是一个占位符，表示这个类没有属性和方法，只是一个空类


#2）创建和使用对象
#创建对象：对象是类的实例，通过类名加括号来创建对象
#animal = Animal()
#print(animal)
#<__main__.Animal object at 0x0000028F40546900>
#print调用对象的__str__方法，返回对象的内存地址
#这种双下划线开头和结尾的方法叫做魔法方法，是Python的特殊方法，用来实现特殊功能


#3）类成员
#类成员包括成员变量（attribute）、属性（property）和成员方法（method）
#成员变量分为类变量和实例变量
#成员方法分为类方法、实例方法和静态方法
#a）
#实例变量：是某个实例独有的数据，通过self变量定义
class Animal(object):
    def __init__(self, name, age): #初始化方法，用来初始化实例变量
        self.name = name
        self.age = age
animal=Animal('dog', 2)
print(animal.name)
print(animal.age)
#b)
#类变量：是所有实例共享的数据，通过类名定义
class Animal(object):
    info = 'cute animal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
print(Animal.info)#访问类变量，通过类名访问，访问示例变量，通过实例名访问
print(animal.__dict__)#访问实例变量，通过实例名访问，返回一个字典，字典的键是变量名，值是变量值
animal.gender = 'male'#给实例添加一个实例变量,一般不推荐这样做
print(animal.__dict__)
#c)
#构造方法：是一种特殊的方法，用来初始化实例变量 __init__方法
#d)
#方法：是类中定义的函数，分为类方法、实例方法和静态方法

#实例方法：第一个参数是self，表示实例本身，通过self可以访问实例变量和实例方法
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):#self可以理解成c语言里的结构体指针
        print('running')
a1 = Animal('dog', 2)
a1.run()#调用实例方法，通过实例名调用

#类方法：第一个参数是cls，表示类本身，通过cls可以访问类变量和类方法
class Account:
    interest_rate = 0.0668
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
    @classmethod#装饰器，用来定义类方法
    def interest_by(cls, amt):#cls表示类本身
        return cls.interest_rate * amt
interest = Account.interest_by(1000)#调用类方法，通过类名调用
print(interest)

#静态方法：没有self和cls参数，通过类名或实例名调用
class Account:
    interest_rate = 0.0668
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
    @staticmethod#装饰器，用来定义静态方法
    def interest_by(amt):#没有self和cls参数
        return Account.interest_rate * amt
interest = Account.interest_by(1000)#调用静态方法，通过类名或实例名调用
print(interest)
#静态方法和类方法相似，定义静态方法只是为了提供一个基于类名的命名空间，使代码更加清晰


#4）封装性
#a）私有变量：在变量名前加双下划线，表示私有变量
#私有变量只能在类的内部访问，不能在类的外部访问
#python中没有真正的私有变量，只是通过改变变量名来实现私有变量
#比如__weight私有变量，实际上是可以通过类名__weight来访问
#b）私有方法：在方法名前加双下划线，表示私有方法
#和私有变量类似
#c）定义属性
#在面向对象设计中，一个类是不应该有公有的实例成员变量的，这些实例成员应该被设计成私有的，然后通过公有的setter和getter访问器来访问
class Animal(object):
    def __init__(self,age,sex,weight=0):
        self.age = age
        self.sex = sex
        self.__weight = weight#定义实例变量，私有变量

    @property#装饰器，用来定义属性
    def weight(self):#定义getter方法
        return self.__weight
    #先定义getter方法，再定义setter方法
    @weight.setter#装饰器，用来定义setter方法
    def weight(self, value):#定义setter方法
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('weight must be positive')
a1=Animal(1,'male',10)
print(a1.weight)#调用getter方法，通过实例名调用
a1.weight = 20#调用setter方法，通过实例名调用
print(a1.weight)#调用getter方法，通过实例名调用
#属性本质上是一个方法，通过@property装饰器定义，通过@属性名.setter装饰器定义setter方法


#5）继承性
#继承是面向对象编程的一种特性，一个类可以继承另一个类的属性和方法，从而实现代码的复用
#a)继承的语法：class 子类名(父类名): object为默认父类
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        template = 'name:{0},age:{1}'
        return template.format(self.name, self.age)

class student(person):
    def __init__(self, name, age, school):
        super().__init__(name, age)#调用父类的构造方法
        self.school = school
    def info(self):
        template = 'name:{0},age:{1},school:{2}'
        return template.format(self.name, self.age, self.school)

#b)重写方法
#子类可以重写父类的方法，重写方法的方法名和参数列表必须和父类的方法完全一致
#重写方法可以改变父类方法的实现，也可以调用父类的方法
class animal(object):
    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def eat(self):
        self.weight += 1
        print('eating')
#重写方法后
class dog(animal):
    def eat(self):
        self.weight +=2
        print('eating')
        return self.weight
a1=dog('dog', 2,10)
print(a1.eat())
a1.eat()

#c)多继承
#一个类可以继承多个父类，多个父类之间用逗号分隔
#多继承的语法：class 子类名(父类名1,父类名2,...): object为默认父类
#当子类继承多个父类时，如果多个父类中有同名的方法，那么子类会调用哪个方法呢？
#答案是，子类会按照父类的继承顺序，从左到右依次查找方法，如果找到了，就调用这个方法，如果找不到，就继续查找下一个父类，直到找到为止
class parentclass1:
    def run(self):
        print('parentclass1 run')
class parentclass2:
    def run(self):
        print('parentclass2 run')
class childclass(parentclass1, parentclass2):
    pass#表示是空类
a1 = childclass()
a1.run()#调用父类的方法，按照继承顺序，先调用parentclass1的方法
class childclass(parentclass2, parentclass1):
    pass
a1 = childclass()
a1.run()#调用父类的方法，按照继承顺序，先调用parentclass2的方法


#6）多态性
#发生多态性的条件：继承，重写方法，父类引用指向子类对象
#多态性优势在于运行期动态特性，其对于python这类动态语言来说意义不大

#类型检查：isinstance(object, classinfo)，用来检查一个对象是否是一个类的实例或子类的实例。
#通过运行期类型检查可以证实python的语言多态性
#在动态语言中有一种类型检查称为‘鸭子类型’


#7）python根类 object

#a）__str__方法：用来返回一个对象的字符串表示，这个方法在print函数中调用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Person(name={}, age={})'.format(self.name, self.age)
p = Person('Tom', 20)
print(p)#调用__str__方法，返回对象的字符串表示

#b)__eq__方法：用来比较两个对象是否相等，这个方法在==运算符中调用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Person(name={}, age={})'.format(self.name, self.age)
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False
p1 = Person('Tom', 20)
p2 = Person('Tom', 20)
print(p1 == p2)#调用__eq__方法，比较两个对象是否相等


#8)枚举类
#枚举类是一种特殊的类，用来定义一组常量
#使用枚举类可以提高代码的可读性和可维护性
#枚举类继承自enum.Enum类

#a)定义枚举类
import enum

class WeekDays(enum.Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
day = WeekDays.MONDAY
print(day)#打印枚举类的值
print(day.name)#打印枚举类的名字
print(day.value)#打印枚举类的值

#b)限制枚举类
#@enum.unique装饰器可以限制枚举类的值唯一
#enum.IntEnum类可以限制枚举类的值必须是整数
import enum

@enum.unique
class WeekDays(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
day = WeekDays.MONDAY
print(day)#打印枚举类的值
print(day.name)#打印枚举类的名字
print(day.value)#打印枚举类的值