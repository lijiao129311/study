import time
now = time.strftime("%Y-%m-%d %H:%M:%S")
print(now)
text = input("请输入你今天的心情：")
with open("F:\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-----------------\n")