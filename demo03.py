# a = input("请输入你的姓名：")
# b = input("请输入你的年龄：")
# try:
#     if int(b) > 18:
#         print("成年了")
#     else:
#         print("未成年")
# except:
#     print("请输入正确的年龄")

# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)

# import random
# a = random.randint(100,1000)
# print(a)

# import pymysql
# db = pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
# try:
#     cur = db.cursor()
#     cur.execute("select * from t_class";)
#     res = cur.fetchall()
# except:
#     print("sql语句错误")


"""
class 声明类的名字
然后类的名字首字母必须大写
面相对象编程
类里面所有的对象都必须传一个参数，叫self
"""


class Geese:
    """大雁类"""
    def __init__(self,beak,wing,claw):
        print("我是大雁类！我有以下特征：")
        print(beak)
        print(wing)
        print(claw)
    def fly(self,state):
        print(state)
"*****************调用***************"
beak_1 = "喙的基部较高，长度和头部的长度几乎相等"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是蹼装的"
wildGoose = Geese(beak_1,wing_1,claw_1)
wildGoose.fly("我飞的时候，一会儿排成个人字，一会排成个一字")  #调用实例方法


