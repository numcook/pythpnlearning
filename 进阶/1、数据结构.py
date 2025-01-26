#python中数据结构主要有序列、集合和字典

#序列结构：列表、元组、字符串、字节序列、range对象、
#操作：索引、分片、加、乘
#1)索引
a=[8,4,3,2,7]
print(a[0])
print(a[-1])#可访问最后一个元素
print(a[1])
print(max(a))  
print(min(a))
print(len(a))
#2)分片
#a[0:3]取前三个元素,【start:end:step】开始索引，结束索引（不包括该位置元素），步长
#step为负数时，start应大于end，表示从后往前取元素
#3)加和乘
#和字符串一样，列表也支持加和乘操作


#元组结构：元组是不可变的序列，元组的元素不能修改
#1）元组的创建
b=(1,2,3,4,5)#或者b=1,2,3,4,5，小括号或不用括号都可以
tuple1=(1,)#只有一个元素时，需要在元素后加逗号
#三种创建元组的方式等价
#2）访问元组
a=('hello','world',1,2,3)
print(a[0])
print(a[1])
print(a[0:2])
#3)元组拆包
#将元组中的元素赋值给多个变量
str1,str2,_,*n=a
#str1='hello',str2='world',n=[2,3]\
#星号表示将剩余元素赋值给n
#下划线表示不需要的元素
#4）遍历元组
for item in a:
    print(item)
for i,item in enumerate(a):
    print(i,item)#enumerate()函数返回元素的索引和值


#列表结构：列表是可变的序列
#1）列表的创建
a=[2,1,3,4,5]#或者a=list((2,1,3,4,5)) list()函数将元组转换为列表
#用[]创建列表，元素之间用逗号隔开
#2)追加元素
a.append(6)#在列表末尾追加元素
a.extend([7,8,9])#在列表末尾追加多个元素
#3)插入元素
#a.insert(1,2)#在索引为1的位置插入元素列表的第一个位置插入元素
#4)替换元素
#a[1]=3#将列表的第二个元素替换为3
#5)删除元素
#a.remove(3)#删除列表中第一个出现的元素3,不返回删除元素
#a.pop(i)#删除索引为i的元素，返回删除元素1的元素，返回删除元素
#若不指定索引，则删除最后一个元素
#6)其他操作
#a.reverse()#反转列表
#a.sort()#排序列表
#a.clear()#清空列表
#a.copy()#复制列表
#a.count(3)#统计元素3在列表中出现的次数
#a.index(3,i,j)#返回元素3在列表中索引，i为起始索引，j为结束索引的索引
a.sort(reverse=True)#降序排列
for item in a:
    print(item)
#7)列表推导式
#推导式可以将一种数据结构转换为另一种数据结构
n=[]
for i in range(10):
    if i%2==0:
        n.append(i**2)
print(n)
#等价于
#n=[i**2 for i in range(10) if i%2==0]
#其中i**2为表达式，for i in range(10)为循环，if i%2==0为条件
#可有多个for循环和if条件


#集合结构：集合是无序的，元素不重复
#1）可变集合的创建
a={1,2,3,4,5}#或者a=set([1,2,3,4,5])
#用{}创建集合，元素之间用逗号隔开
#创建空集合时，不能用{}，因为{}表示空字典，应使用set()函数
#len(a)返回集合中元素的个数
#2)修改可变集合
#a.add(6)#添加元素6
#a.update([7,8,9])#添加多个元素
#a.remove(3)#删除元素3，若元素不存在，则抛出异常
#a.discard(3)#删除元素3，若元素不存在，则不抛出异常
#a.pop()#随机删除一个元素
#a.clear()#清空集合
#3)遍历集合
for item in a:
    print(item)
for i,item in enumerate(a):
    print(i,item)#enumerate()函数返回元素的值和循环次数
#4)不可变集合的创建
a=frozenset([1,2,3,4,5])#不可变集合的创建
#5)集合推导式
#n={i**2 for i in range(10) if i%2==0}
#输出结果是集合，会过滤掉重复元素


#字典结构：字典是无序的键值对集合
#像哈希表，键值对的形式存储数据
#1)创建字典
a={'name':'zhangsan','age':18,'gender':'male'} 
#一般创建方式，键值对之间用逗号隔开，键值对之间用冒号隔开
#或者a=dict(name='zhangsan',age=18,gender='male')
#用dict()函数创建字典
#用=时，键值对的键不能加引号，值可以加引号，且键应是字符串
#或者a=dict([('name','zhangsan'),('age',18),('gender','male')])
#用列表创建字典(用元组也可以)
#2）修改字典
#a['name']='lisi'#修改键为name的值
#del a['name']#删除键为name的键值对
#a.pop('name')#删除键为name的键值对，并返回值
print(a.popitem())#随机删除一个键值对，并返回键值对
#3)访问字典
#a.get('name')#获取键为name的值
#get(key,default)#获取键为key的值，若键不存在，则返回default
#a.keys()#获取所有键
#a.values()#获取所有值
#a.items()#获取所有键值对
#用in not in判断键是否存在
#4)遍历字典
#键和值可以分别遍历，也可以同时遍历
student_dict={'17':'lihua','18':'zhangsan','20':'helen'}
for student_name in student_dict.values():
    print(student_name)
for student_age in student_dict.keys():
    print(student_age)
for student_name,student_name in student_dict.items():
    print('年龄：{0}，姓名：{1}'.format(student_age,student_name))
#5)字典推导式
input_dict={'a':1,'b':2,'c':3,'d':4}
output_dict={key:value**2 for key,value in input_dict.items() if value%2==0}
print(output_dict)
#输出结果为{'b':4,'d':16}
keys={k for k,v in input_dict.items() if v%2==0}
print(keys)
#输出结果为{'b','d'}
