#函数式编程
#函数式编程是一种编程范式，它将电脑运算视为数学上的函数计算，并且避免使用程序状态以及易变对象。
#函数式编程语言最重要的特性是支持高阶函数和函数柯里化。
#高阶函数：一个函数接受另一个函数作为参数，或者返回一个函数，或者两者都具备的函数。
#函数柯里化：将一个多参数的函数转换成多个单参数函数，并且返回一个新函数的技术。
#函数式编程和面向对象编程一样都是一种编程范式

#1）函数类型
#函数是一等公民，可以赋值给变量，可以作为参数传递，可以作为返回值返回。
def add(x,y):
    return x+y
print(type(add))#<class 'function'>

#2)lambda表达式
#lambda表达式是一种匿名函数，它可以在一行中定义一个简单的函数。
#lambda表达式的基本语法是：lambda 参数列表: 表达式
#lambda表达式只能包含一个表达式，不能包含复杂的逻辑。
#lambda表达式通常用于简单的函数，例如排序、过滤等。
def calculate(opr):
    if opr=='add':
        return lambda x,y:x+y
    elif opr=='sub':
        return lambda x,y:x-y
    elif opr=='mul':
        return lambda x,y:x*y
    elif opr=='div':
        return lambda x,y:x/y
    else:
        return lambda x,y:x**y
f1=calculate('add')#f1是一个函数
print(f1(2,3))#5


#3)三大基础函数
#过滤、映射和聚合是函数式编程的三大基础函数。

#a)过滤函数
#过滤函数用于过滤一个序列，返回一个新序列。
number_list = range(1,10)
number_filter = filter(lambda x:x % 2 == 0, number_list)
print(list(number_filter))#[2, 4, 6, 8]

#b)映射函数
#映射函数用于对一个序列的每个元素进行操作，返回一个新序列。
number_list = range(1,10)
number_map = map(lambda x:x*2, number_list)
print(list(number_map))#[2, 4, 6, 8, 10, 12, 14, 16, 18]

#c)聚合函数
#聚合函数用于对一个序列进行聚合操作，返回一个值。
#reduce(function,iterable[,initializer])iterable是一个序列，initializer是初始值。
from functools import reduce
number_list = range(1,10)
number_reduce = reduce(lambda x,y:x+y, number_list)
print(number_reduce)#45
number_reduce = reduce(lambda x,y:x+y, number_list, 10)
print(number_reduce)#55
