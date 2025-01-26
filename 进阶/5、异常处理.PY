#python中异常根类是BaseException，所有异常类都继承自该类
#其中异常类命名主要后缀有Error、Exception和Warning
#Error是程序错误，通常由于逻辑错误导致，如IndexError、KeyError等
#Exception是程序异常，通常由于外部原因导致，如IOError、ValueError等
#Warning是程序警告，通常用于提示用户注意，如DeprecationWarning、UserWarning等


#1）常见异常
#a）AttributeError：属性错误，当尝试访问一个类中不存在的成员而引发的异常
#b）OSError：操作系统错误，当操作系统无法执行某个操作时引发的异常。例如，文件不存在、权限不足等
#c)IndexError：索引错误，当尝试访问一个序列中不存在的索引时引发的异常
#d）KeyError：键错误，当尝试访问一个字典中不存在的键时引发的异常
#e)NameError：名称错误，当尝试访问一个不存在的变量时引发的异常
#f)TypeError：类型错误，当尝试将一个操作应用于一个不支持的类型时引发的异常
#g)ValueError：值错误，当尝试将一个不合适的值赋给一个对象时引发的异常


#2)捕获异常
#当前函数有能力解决，则捕获异常进行处理，否则抛出异常给上层调用者处理。

#try:
#    #可能引发异常的代码
#except Exception as e:#可以有多个except，捕获不同类型的异常
#    #处理异常的代码    #当一个except捕获到异常后，后面的except将不再执行
                       #如果异常存在父子类关系，则子类异常应放到父类前捕获，否则子类异常将无法捕获

#try-except语句也可以嵌套使用，以便在捕获异常后进行更详细的处理。但尽量避免嵌套，以免代码结构混乱。
#如果多个except语句中的异常处理相同，可以将多个异常列为元组一起处理
#excpt （Exception1,Exception2）as e:


#3）异常堆栈跟踪
#当程序发生异常时，Python会打印异常堆栈跟踪信息，包括异常类型、异常值和异常发生的位置等信息。
#异常堆栈跟踪信息可以帮助我们了解异常发生的原因和位置，以便我们能够更好地调试程序。
#可以使用traceback模块提供的print_exc()来获取异常堆栈跟踪信息。
#traceback.print_exc(limit=None,file=None, chain=True)
#其中参数limit限制堆栈跟踪的个数，默认None不限制
#file判断是否输出堆栈信息到文件，默认为None是不输出到文件
#chain表示是否打印异常链，默认为True
#例如：
import datetime as dt
import traceback as tb

def read_file(filename):
    try:
        file=open(filename)
        data=file.read()
        date=data.strip()
        return dt.datetime.strptime(date,"%Y-%m-%d")
    except (ValueError, OSError) as e:
        tb.print_exc()
        return None


#4）释放资源
#有时，在执行某些操作时需要释放资源，如文件、网络连接等。如果程序在执行过程中发生异常，那么这些资源可能无法被正确释放。
#try-finally语句或with as自动资源管理可以用来释放资源，无论是否发生异常，finally语句中的代码都会被执行。
#与while和for循环类似，try语句也可以带有else语句，当try语句中的代码没有引发异常时，else语句中的代码会被执行。

import datetime as dt

def read_file(filename):
    try:
        file=open(filename)
    except OSError as e:
        print("文件打开失败")
    else:
        print("文件打开成功")
        try:
            data=file.read()
            date=data.strip()
            return dt.datetime.strptime(date,"%Y-%m-%d")
        except ValueError as e:
            print("日期格式错误")
        finally:
            file.close()

#with as自动资源管理
#with语句可以用来自动管理资源，当with语句块中的代码执行完毕后，资源会被自动释放，无论是否发生异常。
#with语句的语法如下：
#with expression [as variable]:
#    with_suite

import datetime as dt
import traceback as tb

def read_file(filename):
    try:
        with open(filename) as file:
            data=file.read()
        date=data.strip()
        return dt.datetime.strptime(date,"%Y-%m-%d")
    except (ValueError, OSError) as e:
        tb.print_exc()
        return None


#5）自定义异常类
#Python允许我们自定义异常类，以便在程序中抛出自定义的异常。自定义异常类需要继承自Exception类或其子类。
#自定义异常类可以定义一些属性和方法，以便在抛出异常时传递更多的信息。
#例如：
class MyException(Exception):
    def __init__(self, message):#message是异常信息
        super().__init__(message)
        self.message = message
    def __str__(self): 
        return self.message


#6）显示抛出异常
#之前的异常都是由系统生成的，我们也可以手动抛出异常。使用raise语句可以抛出异常，raise语句后面可以跟一个异常类或异常实例。
#例如：
#except ValueError as e:
#   raise ValueError("日期格式错误")
