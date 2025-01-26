#函数语法基础

#1)定义函数语法格式
# def 函数名(参数列表):
#     函数体
#     return 返回值

def add(a,b):
    return a+b
print(add(1,2))


#2)函数参数
def area(width,height):
    return width*height
print(area(2,3))#位置参数传递参数
print(area(width=2,height=3))#指定参数名传递参数
#参数形式统一


#3)参数默认值
#在定义函数时，可以给参数指定默认值，调用函数时，如果没有传递参数，则使用默认值
def make_coffee(name='卡布奇诺'):
    return '制作一杯'+name
print(make_coffee())#制作一杯卡布奇诺
print(make_coffee('拿铁'))#制作一杯拿铁


#4)可变参数
#如果参数个数不确定，可以使用可变参数，可变参数在函数定义时，参数名前加*或**
#a)加*时，可变参数是一个元组
def sum(*numbers,mutiplier):
    result=0
    for number in numbers:
        result+=number
    return result*mutiplier
print(sum(1,2,3,4,5,mutiplier=2))#30
double_tuple=(6,7)
print(sum(1,*double_tuple,mutiplier=2))#28
#*将元组拆包成位置参数传递给函数
#b)加**时，可变参数是一个字典
def show_info(sep=':',**info):
    result=''
    for key,value in info.items():
        result+=key+sep+value+'\n'#此语句要求key、value、sep都是字符串
    return result
print(show_info(name='张三',age='18',gender='男'))
stu_info={'name':'李四','age':'19','gender':'女'}
print(show_info(sep='_',**stu_info))
#**将字典拆包成关键字参数传递给函数
#可变参数可以同时使用，但*参数必须在关键字参数和**参数前面
def show_info1(*args,sep=':',**kwargs):
    for key,value in kwargs.items():
        print("{0}{1}{2}".format(key,sep,value))
    i=0
    for arg in args:
        i+=arg
    return i
print(show_info1(sep='_',name='王五',age='20',gender='男'))
print(show_info1(1,2,3,4,5,6,sep='_',name='赵六',age='21',gender='女'))


#5)函数返回值
#无返回值时，可以省略return语句，或者return None
#可以返回多个值，返回值是一个元组
def position(dt,*speed):
    posx=dt*speed[0]
    posy=dt*speed[1]
    return posx,posy
move=position(60,10,-1)
print("移动矢量=({0},{1})".format(move[0],move[1]))
#或者posx,posy=position(60,(10,-1))


#6)函数变量作用域
#全局变量：在函数外部定义的变量，可以在函数内部使用
#局部变量：在函数内部定义的变量，只能在函数内部使用
#如果函数内部需要修改全局变量，可以使用global关键字声明
def change():
    global a
    a=100
change()
print(a)
#如果函数内部需要修改外部变量，可以使用nonlocal关键字声明
def outer():
    b=10
    def inner():
        nonlocal b
        b=20
    inner()
    print(b)
outer()


#7)生成器
#生成器是一种特殊的迭代器，使用yield关键字定义
#生成器函数：使用yield关键字定义的函数，调用函数时，返回一个生成器对象
#生成器对象：调用生成器函数返回的对象，可以使用next()函数获取下一个值
#生成器函数执行到yield语句时，会暂停执行，返回yield后面的值
def my_gen():
    yield 1
    yield 2
    yield 3
gen=my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
#生成器函数可以包含多个yield语句，每次调用next()函数，会执行到下一个yield语句
def squares(n):
    for i in range(n):
        yield i**2
for i in squares(5):
    print(i)
#生成器表达式：类似列表推导式，使用()包裹，返回一个生成器对象


#8)嵌套函数
#在函数内部定义函数
def outer():
    def inner():
        print('inner')
    inner()
outer()
#内部函数可以访问外部函数的变量
#在外部函数外部不能调用内部函数
def calculate(n1,n2,opr):
    def add():
        return n1+n2
    def sub():
        return n1-n2
    if opr=='+':
        return add()
    elif opr=='-':
        return sub()
print(calculate(1,2,'+'))
print(calculate(1,2,'-'))



