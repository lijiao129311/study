"""
练习
"""
a = input("请输入：")
b = input("请输入：")
print("两段字符的长度是：",len(a) + len(b))

"""
联习：
获取用户的个人信息，存储到字典中
信息有：name,age,sex
"""
name = input("请输入你的姓名：")
age  = input("请输入你的年龄：")
sex  = input("请输入你的性别：")
user = {}
# user.update(name=name,age=age,sex=sex)
user["name"] = name
user["age"] = age
user["sex"] = sex
print(user)


"""
练习题:方法1(while)
"""
hightgrade = {}
lowergrade = {}
studentlist = ["张三","李四","王二","李雷","王磊","何时","流云","王洋","何彬","菲亚"]
a = 0
while a < len(studentlist):
    grade = int(input("请输入"+studentlist[a]+"的成绩："))
    if grade >= 60:
        hightgrade[studentlist[a]] = grade
    else:
        lowergrade[studentlist[a]] = grade
    a = a + 1

print("成绩大于60分的学生有：",hightgrade)
print("成绩小于60分的学生有：",lowergrade)

"""
练习题：方法2(for)
"""
hightgrade = {}
lowergrade = {}
studentlist = ["张三","李四","王二","李雷","王磊","何时","流云","王洋","何彬","菲亚"]
for i in studentlist:
    grade = int(input("请输入"+i+"的成绩："))
    if grade >= 60:
        hightgrade[i] = grade
    else:
        lowergrade[i] = grade

print("成绩大于60分的学生有：",hightgrade)
print("成绩小于60分的学生有：",lowergrade)

"""
练习:
打印九九乘法口诀表
"""

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"×",i,"=",j*i,end="  ")
    print()

"""
练习1：
通过print打印,模拟一个红绿灯的功能。注意：红灯30次，绿灯35次，黄灯3次
练习2：
通过代码，实现一个用户注册功能。
用户输入账号和密码，要求账号长度是5-8位，密码长度是6-12位，
并且账号必须以小写开头，储存到字典中，{username:password}
"""
# a = 0
# while a == 0:
#     for i in range(30,0,-1):
#         print("红灯还有"+str(i)+"秒结束")
#     for j  in range(35,0,-1):
#         print("绿灯还有"+str(j)+"秒结束")
#     for k in range(3,0,-1):
#         print("黄灯还有"+str(k)+"秒结束")


light = {"红灯":30,"绿灯":35,"黄灯":3}
while True:
    for i in light:
        for j in range(light[i]):
            print(i,"倒计时还有",light[i]-j,"秒")


username = input("请输入账号：")
password = input("请输入密码：")
if len(username) >= 5 and len(username) <= 8:
    if username[0] in "abcdefghijklmnopqrstuvwxyz":
        if len(password) >= 6 and len(username) <= 12:
            print("注册成功！",{username:password})
        else:
            print("密码必须6-12位！")
    else:
        print("账号必须以小写字母开头")
else:
    print("请输入5-8位账号")

"""
练习
定义一个方法，用来判断用户输入的账号和密码是否符合规范。
"""



def checkname(username,password):
    """
    自动检查账号的长度是5-8位，密码长度是6-12位，并且账号必须以小写开头
    """
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "abcdefghijklmnopqrstuvwxyz":
            if len(password) >= 6 and len(password) <= 12:
                return True
            else:
                return "密码不符合规范"
        else:
            return "账号的首字母必须以小写字母开头"
    else:
        return "账号的长度不符合规范，请输入5-8位账号"

checkname(username,password)