#python中的数据持久化技术：
#1.将数据保存到文件中
#2.将数据保存到数据库中

#python中将数据保存到数据库中的技术主要分为两类：
#1.使用数据库API 编写MySQL语句
#2.使用ORM框架  对象映照关系映射

#......安装oracle的社区板MySQL Community Edition 

#1）链接MySQL数据库
#方法一：通过MySQL 5.7 Command Line Client 链接MySQL数据库
#方法二：通过命令行mysql -hlocalhost -u root -p链接MySQL数据库 （需现将根目录添加至环境变量中）

#2）常见数据库管理命令（默认加分号）
#help：查看帮助，不加分号
#show databases：查看当前数据库
#create database 数据库名：创建数据库
#drop database 数据库名：删除数据库
#use 数据库名：切换数据库，不加分号
#show tables：查看当前数据库中的表
#desc 表名：查看表结构

#以下链接方式主要为使用数据库API编写MySQL语句，遵循SQL语法Python DP-API规范
#1）建立数据连接
#使用Pymysql模块连接MySQL数据库
#pymysql.connect()常用连接参数：
#host：数据库主机名或IP地址
#port:连接数据库端口号
#user：访问数据库账号
#password：访问数据库密码
#database：数据库名称
#charset：字符编码
#等等
#连接成功后，返回Connection对象
#connection有如下常用方法：
#cursor()：返回Cursor游标对象
#commit()：提交数据库事务
#rollback()：回滚数据库事务
#close()：关闭数据库连接
#返回Cursor对象有如下常用基本sql操作方法：
#execute(sql语句，参数)：执行一条SQL语句，参数可是序列或字典，返回值为受影响的行数
#executemany(sql语句，参数)：执行多条SQL语句，参数为序列，返回值为受影响的行数
#callproc(procname，参数)：执行存储过程proname
#excute()方法和executemany()方法都返回受影响的行数，对于查询语句，使用fetchone()方法或fetchmany()或fetchall()方法获取查询结果

#对数据库表中数据可以进行增删改查操作
#数据库编程步骤：
#1.建立数据库连接
#2.创建游标对象
#3.编写SQL语句
#4.执行SQL语句
#5.获取查询结果
#6.关闭数据库连接

#以下为一个通过JDBC技术实现python对数据的CURD操作
#数据库名为testdb
#a)select name,userid from user where userid > ? order by userid 有条件查询
import pymysql

#1）建立数据库连接
connection = pymysql.connect(host='localhost', user='root', password='5415443a@', database='testdb', charset='utf8')
try:
#2）创建游标对象
    with connection.cursor() as cursor:#with语句会自动关闭游标对象
        #3）编写SQL语句
        sql = "select name,userid from user where userid > %(id)s"

        #4）执行SQL语句
        cursor.execute(sql,{'id':0})

        #5）获取查询结果
        result = cursor.fetchall()
        for row in result:
            print('name=%s,userid=%d' % (row[0], row[1]))
finally:
    #6）关闭数据库连接
    connection.close()

#b）select max(userid) from user 无条件查询
import pymysql

#1）建立数据库连接
connection = pymysql.connect(host='localhost', user='root', password='5415443a@', database='testdb', charset='utf8')
try:
#2）创建游标对象
    with connection.cursor() as cursor:#with语句会自动关闭游标对象
        #3）编写SQL语句
        sql = "select max(userid) from user"

        #4）执行SQL语句
        cursor.execute(sql)

        #5）获取查询结果
        row = cursor.fetchone()
        if row is not None:
            print('max(userid)=%d' % (row[0]))
finally:
    #6）关闭数据库连接
    connection.close()

#c）insert into user(name,userid) values(?,?) 插入数据
import pymysql

#1）建立数据库连接
connection = pymysql.connect(host='localhost', user='root', password='5415443a@', database='testdb', charset='utf8')
try:
    #2）创建游标对象
    with connection.cursor() as cursor:#with语句会自动关闭游标对象
        #3）编写SQL语句
        sql = "insert into user(userid,name) values(%s,%s)"

        #4）执行SQL语句
        cursor.execute(sql,(3,'Hank'))

        #5）提交事务
        connection.commit()
except pymysql.DatabaseError as e:
    #6）回滚事务
    connection.rollback()
    print(e)
finally:
    #7）关闭数据库连接
    connection.close()

#d）数据库表的更新
#update user set name=? where userid>?
import pymysql

#1）建立数据库连接
connection = pymysql.connect(host='localhost', user='root', password='5415443a@', database='testdb', charset='utf8')
try:
    #2）创建游标对象
    with connection.cursor() as cursor:#with语句会自动关闭游标对象
        #3）编写SQL语句
        sql = "update user set name=%s where userid>%s"

        #4）执行SQL语句
        affectedcount=cursor.execute(sql,('Jack',1))
        print('受影响的行数=%d' % affectedcount)
        #5）提交事务
        connection.commit()
except pymysql.DatabaseError as e:
    #6）回滚事务
    connection.rollback()
    print('发生异常：%s' % e)
finally:
    #7）关闭数据库连接
    connection.close()

#e）数据库表的删除
#delete from user where userid>?
import pymysql

#1）建立数据库连接
connection = pymysql.connect(host='localhost', user='root', password='5415443a@', database='testdb', charset='utf8')
try:
    #2）创建游标对象
    with connection.cursor() as cursor:#with语句会自动关闭游标对象
        #3）编写SQL语句
        sql = "delete from user where userid=%s"

        #4）执行SQL语句
        affectedcount=cursor.execute(sql,(3,))
        print('受影响的行数=%d' % affectedcount)
        #5）提交事务
        connection.commit()
except pymysql.DatabaseError as e:
    #6）回滚事务
    connection.rollback()
    print('发生异常：%s' % e)
finally:
    #7）关闭数据库连接
    connection.close()


# NoSQL数据存储
#不通过SQL语句操作数据库，而是通过键值对的方式存储数据
#python内置dbm模块提供了存储dbm数据的api

#打开dbm数据库
#dbm.open(filename,flag=‘mode’)
#filename：数据库文件名
#flag：打开模式，r只读，w只写，c读写，n新建，e新建并读写
#close()：关闭数据库

#dbm数据存储
#写入数据：d[key]=value，若已存在key，则覆盖
#读取数据：value=d[key]或value=d.get(key，default)，若不存在key，则返回default
#删除数据：del d[key]
#查找数据：flag=key in d
