'''
print("Hello World!")  #字符串
print(2333)    #整数
print(2.333)   #小数
print(True)    #布尔值
print((1,2))   #元组
print([1,2])   #数组
print({1,2})  #字典


锄禾日当午 汗滴禾下土 
谁知盘中餐 粒粒皆辛苦


print("呵呵",233,2.333,True)
print("哈哈"+"嘻嘻")
print("哈哈"*10)
print(((1+2)*100-90)/2)
print(1+1==2)

#变量
#赋值
name = "王凯"
print(name)
'''



#数据格式的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = float(input("请输入 ："))
# b = float(input("请输入 ："))
# print("input获取的内容: ",a+b)

# a = input("请输入：")
# b = input("请输入：")
# print("两段字符的长度是：",len(a) + len(b))

#元组，下标，从0开始编号
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a[-1])
#切片
# print(a[:4])  #左闭右开
# print(a[4:9])
# print(a[9:])


# print(a.index("哈哈"))
# print(a.count("哈哈"))

#二维元组
# b = (a,"哈哈","嘻嘻")
# print(b[0][3])

#数组
# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# a.append("append1")
# a.append("append2")
# print(a)
# a.insert(4,"insert")
# print(a)
# b = a.pop(0)  # 剪切
# c = a.pop(0)  # 剪切
# print(b+c)
# print(a)
# print(b)
# print(c)
# # a.clear()
# # print(a)
# n = ["中国","美国"]
# # a.extend(n)
# print(a+n)

# print(a)
# b = a.remove(1)
# print(b)
# print(a)

# x = [0,False,1,True]
# t = x.count(0)
# print(t)

#下标不要超出范围=越界
# x = [a,1,2,3,4]
# a[5] #越界

"""
python的语法
所有的方法都用小括号结尾，如print()，input()，count()，insert()
元组、数组、字典的取值，都用中括号，如a[0]
元组、数组、字典的定义，分别用()，[]，{}
"""

"""
字典的特点
1、字典中的值没有顺序.
2、字典的结果必须是键值对. 如：key:value
3、字典的取值是通过key去取value
"""
a = {"name":"张三",0:"哈哈","age":25}
#取值
print(a["name"])
#新增
a["hight"] = "183cm"
print(a)
#修改
a["name"] = "李四"
print(a)

b = a.get("name")
print(b)
b = a.pop("name")
print(b)
print(a)
a.update(name="哈哈")
print(a)

print("-------------------")

print(a["name"])
print(a.get("name1"))

#数组和字典的删除用del
del a["name"]
print(a)

# del a[0]

"""
联系：
获取用户的个人信息，存储到字典中
信息有：name,age,sex
"""
print("请输入个人的信息，name: ,age: ,sex: ")
a = input()
print(dict(a))