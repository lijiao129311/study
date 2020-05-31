#判断
# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("你应该退休了！")
# elif age > 30:
#     print("你的家庭责任应该很重吧！")
# elif age > 20:
#     print("你一定要好好规划你的未来！")
# else:
#     print("你一定要好好学习！")


# if age > 20 and age <= 30:
#     print("你一定要好好规划你的未来！")
# elif age > 30 and age < 60:
#     print("你的家庭责任应该很重吧！")
# elif age > 60:
#     print("你应该退休了！")
# else:
#     print("你一定要好好学习！")


# a = "你好"
# if a in ["你好","不好"]:
#     print("OK")
# else:
#     print("NOT OK")

# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄!")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")

# a = "asgjhkhkh"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串！")
# else:
#     print("其他！")

# a = 1
# while a < 10:
#     print("呵呵呵呵",a)
#     a = a + 2

#for循环
# a = "你好，今天你真好看！"
# a = ["张三","李四","王二","李雷","王磊","何时","流云","王洋","何彬","菲亚"]
# for i in a:
#     print(i,end=" ")
  

# b =list(range(0,100,5))  #生成一个数组 步进/步长
# print(b)

# for i in range(100):
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"×",i,"=",j*i,end="  ")
#     print()
        

# for i in range(10):
#     if i == 4:
#         break
#     print(i)


# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == 3:
#             break
#         print(j,"×",i,"=",j*i,end="  ")
#     print()



# def checkname(username):
#     """
#     自动检查账号的长度是5-8位，并且账号必须以小写开头
#     """
#     if len(username) >= 5 and len(username) <= 8:
#         if username[0] in "abcdefghijklmnopqrstuvwxyz":
#             return True
#         else:
#             return "账号必须以小写字母开头"
#     else:
#         return "请输入5-8位账号"

# username = input("请输入账号：")
# password = input("请输入密码：")
# if checkname(username) == True:
#     if len(password) >= 6 and len(password) <= 12:
#         print("注册成功！",{username:password})
#     else:
#         print("密码必须是6-12位")
# else:
#     print(checkname(username))



#def 函数的声明
#checkname 函数的名字
#username 函数的参数
#""""方法的说明"""
#函数的逻辑代码

def add(a,b):
    """
    这个函数的作用是实现两个数的加法
    """
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "你输入的数据类型不正确"

try:
    print(3+dgh)
except Exception as e:
    print("输入的代码有错误",e)

# print(1+ghjk)
