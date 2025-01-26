#标识符和c语言类似
#关键字False、None、True 大写
#声明变量不需要指定类型
#最好一行一个语句，如果一行多个语句用分号隔开
#支持链式赋值
#导入包或函数可以用import或from...import
#支持复数
a = (1+2j)+ (2+3j)
print(a)#(3+5j)
#支持布尔类型
print(1>2)#False
print(1<2)#True
print(bool(1))#True
print(bool(2))#True
print(bool(0))#False

#字符串表示
#1）普通字符串用单引号或双引号括起来
#2）多行字符串用三个单引号或三个双引号括起来
#3）字符串可以用+拼接，可以用*重复
#4）原始字符串用r''表示，不转义
print(r'hello\world')
#5)常见转义字符：\n换行，\t制表符，\r回车，\\反斜杠，\'单引号，\"双引号
# 6)字符串格式化
# %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数 %e 科学计数法 %g 根据值的大小决定使用%f或%e 
name='Tom'
age=20
h=1.75
print('My name is %s, I am %d years old, my height is %.2f'%(name,age,h))#My name is Tom, I am 20 years old , my height is 1.75
#7)字符串查找
#find()返回第一次出现的位置，没有返回-1
#rfind()返回最后一次出现的位置，没有返回-1
source='hello world'
print(source.find('l'))#2
print(source.find('l',2,7))#3,从3到7之间查找
print(source.rfind('l',2,7))
print(source.rfind('l'))#9
#8)字符串转换
#int()将字符串转换为整数
#float()将字符串转换为浮点数
#str()将其他类型转换为字符串

#运算符
#1）算术运算符：+ - * / % // 地板除法：求小于a除以b商的最大整数 ** 幂运算
#2）比较运算符：> < >= <= == !=
#3）逻辑运算符：and逻辑与 or逻辑或 not逻辑非
#4）位运算符：& 按位与：取1的交集
#  | 按位或 ：取1的并集 
# ^ 按位异或：两位相反取一
#  ~ 按位取反 << 左移 >> 右移
#5）赋值运算符：= += -= *= /= %= //= **= &= |= ^= ~= <<= >>=
#6）测试运算符：in not in is is not
#7）运算优先级：算术运算符>位运算符>关系运算符>逻辑运算符>赋值运算符

