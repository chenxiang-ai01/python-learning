#1.input()输入函数
#input(prompt) prompt是提示，会在控制台中显示
#name = input("请输入姓名：")
#print(name)
#pwd = input("请输入你的密码:")
#print(pwd)
#2.转义字符
#2.1\t 制表符 通常表示空一个字符，也称缩进
print('xiao\ao')
print("姓名\t年龄\t电话")

#2.2 \n 换行符
print(end = '\t')
print('haha')

print('哈哈\n嘻嘻')

#2.3\r 回车 表示将当前位置移到本行开头
print('chenxiang\rxiaomao')#简称覆盖
#2.4 \\ 反斜杠符号
print('xiao\\tmao')#为了打些斜号\
print(r"six\\\tar") #r原声字符串，默认取消转义