#math模块
#math.ceil() 向上取整
#math.floor() 向下取整
#round() 四舍五入
#math.sqrt() 开平方
#math.pow(a,b) a的b次方幂运算
#math.log(a,b) a以b为底的对数
#math.pi 圆周率
#math.e 自然常数e
#math.sin() 正弦
#math.cos() 余弦
#math.tan() 正切
#math.asin() 反正弦
#math.acos() 反余弦
#math.atan() 反正切
#math.degrees() 将弧度转换为角度
#math.radians() 将角度转换为弧度


#random模块
#random.random() 生成一个0-1之间的随机小数
#random.randint(a,b) 生成一个a-b之间的随机整数
#random.randrange(a,b) 生成一个a-b之间的随机浮点数
#random.randrange(a,b,step) 生成一个a-b之间的随机浮点数，step为步长
#random.choice() 从一个列表中随机选择一个元素
#random.sample() 从一个列表中随机选择n个元素，返回一个列表q
#random.shuffle() 将一个列表中的元素随机打乱


#datetime模块
#datetime模块有以下几个类：date、time、datetime、timedelta、tzinfo,分别对应于日期、时间、日期时间、时间间隔、时区信息
#1）datetime类
import datetime
dt=datetime.datetime(2025,1,22)
print(dt)
#datetime.today() 返回日期中的天,本地时间
#datetime.month() 返回日期中的月
#datetime.year() 返回日期中的年
#datetime.now(tz=None) 返回当前日期和时间
#datetime.utcnow() 返回当前UTC日期和时间，不包含时区信息
#datetime.fromtimestamp(timestamp,tz=None) 根据UNIX时间戳(自1970年1月1日0时0分0秒以来的秒数)
#datetime.utcfromtimestamp(timestamp) 根据UNIX时间戳(自1970年1月1日0时0分0秒以来的秒数)生成一个datetime对象返回UTC日期和时间

#2）date类
#date.today() 返回当前日期
#date.fromtimestamp(timestamp) 根据UNIX时间戳(自1970年1月1日0时0分0秒以来的秒数)生成一个date对象

#3）time类

#4）日期时间计算
d=datetime.date.today()
delta=datetime.timedelta(5)
print(d+delta)

#5）日期时间格式化和解析
#datetime.strftime(format) 将日期时间格式化为字符串
#datetime.strptime(date_string,format) 将字符串解析为日期时间
#datetime.strftime("%Y-%m-%d %H:%M:%S") 将日期时间格式化为字符串
#datetime.strptime("2025-01-22 12:30:00","%Y-%m-%d %H:%M:%S") 将字符串解析为日期时间
#  %_ 表示日期显示的格式，%Y表示年份，%m表示月份，%d表示日期，%H表示小时，%M表示分钟，%S表示秒

#6）时区信息
           

#logging模块
#当程序运行时，如果遇到错误，程序会停止运行，并输出错误信息，这些信息被称为日志。Python提供了logging模块，用于记录日志信息。
#logging模块可以同时输出日志信息和时间、所在函数、所在线程等，方便开发者调试程序。
#logging模块有以下几个函数：logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical()，分别对应于调试、信息、警告、错误和严重错误级别。级别由低到高

import logging
logging.basicConfig(level=logging.ERROR,format='%(name)s-%(asctime)s - %(levelname)s - %(message)s')
#level设置日志级别，format设置日志格式
#高于等于设置级别的日志才会被记录
#日志格式参数有：%(name)s 日志器名称，%(asctime)s 日志时间，%(levelname)s 日志级别，%(message)s 日志信息
#%(thread)d 线程ID，%(threadName)s 线程名称，%(process)d 进程ID，%(processName)s 进程名称，%(filename)s 文件名，%(funcName)s 函数名，%(lineno)d 行号
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
#输出的日志信息中root表示日食输出对象是root日志器
#使用getLogger(name)函数可以获取一个日志器对象，name参数是日志器的名称，如果不指定name参数，则默认为root

#日志信息默认输出到控制台，也可以日志信息输出到文件中
#logging.basicConfig(level=logging.ERROR,format='%(name)s-%(asctime)s - %(levelname)s - %(message)s',filename='log.txt')
#filename参数指定日志文件名，如果不指定filename参数，则默认输出到控制台

#使用配置文件配置日志信息

