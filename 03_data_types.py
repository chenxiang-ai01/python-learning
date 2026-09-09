#3.1 int整型（常用）：任意大小的整数
num = 1
#检测数据类型的方法type（）
#print(type(num))
#3.2float浮点数：小数
num2 = 1.5
#print(type(num2))
#3.3bool布尔型（重点）
#有固定写法，一个为True，一个为False 注意大小写
#print（type(True))
#布尔值可以当作整型来对待，True相当于整数1，False相当于0
#print(True+False) #1 + 0 = 1
#3.4complex复数型（了解）
#固定写法 ： z = a + bj ---a是实部，b是虚部，j是虚数单位
print(type(2+3j)) #j是固定的虚数单位

#4.字符串str
#特点： 需要加上引号
name = 'sixstar'
print(name)

#5.格式化输出
#5.1占位符
#生成一定格式的字符串
#5.2 %
#1. %s字符串（常用）
name = ('ninging')
print("我的名字:%s"%name)#占位符只是占据位置，并不会输出

#%d 整数（常用）
age = 18
name = 'chenxiang'
print("我的名字：%s，年龄：%d"%(name,age))

#%4d 整数
#数字设置位数，不足补前面空白
a = 123
print("%06d"%a) #表示输出的整数显示位数，不足的话用0补全，超出当前位数则原样输出

#4.%f 浮点数（常用）
a = 1.3
print("%f"% a) #默认后六位次小数，遵循四舍五入原则

#5.%.4f 浮点数
#数字设置小数位数，一样遵循四舍五入
b = 2.34567
print("%.3f"% b) #默认显示7位小数

#6.%%
print("我是%%的1%%" %())

#5.3f格式化
#格式：f"(表达式）”
name = 'xiang'
age = 18
print(f"我的名字是{name}，年龄是{age}")


