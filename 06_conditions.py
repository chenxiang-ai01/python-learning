#1.if判断基本格式
#if 判断条件：
     #满足条件做的事情

#age = 17
#if age < 18:
    #print('未成年不能上网')
#用户从控制台输入成绩，如果满分，输出‘你真棒！’，如果60分，输出‘还要继续加油哈！’
#score = input('请输入成绩：')
#if score == '100':
    #print('你真棒')
#if score == '60':
    #print('还要继续加油哈')
#2.比较运算符
#==比较的是俩个变量的值是否相等，相等的话返回为True，不相等返回为False
#！=（不等于）比较的是俩个变量的值是否相等，不相等的话返回为True，相等返回为False
a = 666
b = 999
#print(a != b)  #结果为True
if a < b:
    print('a小于b')

#3.逻辑运算符
# and 左右俩边都符合才为真
# or 左右俩边只需要符合一个
a = '哈哈'
b = '嘿嘿'
if a == '哈哈' and b == '嘿嘿':
    print("a和b都在笑")

#3.not 表示相反的结果
print(not 3>9)

#4.三目预算（三元表达式）
#基本格式：为真结果 if 判断条件 else 为假结果

#5.if else
#基本格式：
#if 条件：
       #满足条件时要做的事情
#else：
#      不满足条件时要做的事情
a = 666
if a == 666:
    print("你真棒")
else:   #不加任何东西在else后面
    print("还要继续加油")
    #4.三目预算（三元表达式）
    # 基本格式：为真结果 if 判断条件 else 为假结果
a = 5
b = 8
#if a <= b:
    #print("a小于等于b")    #为真结果
#else:
    #print("a比b大")       #为假结果
print("a小于等于b") if a <= b else print("a比b大")

#6.if-elif结构
#if-else 二选一 if-elif多选一
#if 条件1:
    #满足条件1要做的事情1
#elif 条件2:
    #满足条件2要做的事情
score = 85
if 85 <= score <= 100:
    print("优秀")
elif 60 <= score < 85:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("成绩无效")
    #else可以表示所有条件都不符合的情况

#7.f嵌套
#if 条件1:
 #   事情1
  #  if 条件2:
   #     事情2
#else:
 #   不满足条件做的事情
#注意： 内层if判断和外层if判断都可以是if-else结构

#定义一个布尔型变量，表示是否有车票
ticket = True  #True代表有车票，False代表没车票
#定义一个浮点型变量，来保存体温
temp = 36.5
if ticket == True: #外层if判断
    print("可以进站-->",end="")
    if 36.3 <= temp <= 37.2:
        print("体温正常，安心回家")
    else:
        print("体温异常，抓去隔离")
else:
    print("没票不能进站")





