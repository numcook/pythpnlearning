#条件语句
##import sys
#score = int(sys.argv[1])
#if score >= 90:
#    print("优秀")
#elif score >= 80:
#    print("良好")
#elif score >= 70:
#    print("中等")
#elif score >= 60:
#    print("及格")
#else:
#    print("不及格")

#循环语句

#while循环
i=0
while i*i<1000:
    i+=18
print('i = {0}'.format(i))

#for循环
for i in range(1,10):
    print("{0} * {1} = {2}".format(i,i,i*i))
for item in 'hello':
    print(item)
for num in [1,2,3,4,5]:
    print(num)
else:
    print('循环结束')
#跳转语句
for i in range(1,10):
    if i%2==0:
        continue#跳过本次循环
    print(i)
    if i==5:
        break#跳出循环

#range()函数
#range(start,stop,step)