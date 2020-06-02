# 计算1-100求和
sum = 0
for i in range(101):
    sum += i
print(sum)

# 加入分支结构实现1~100之间的偶数求和
sum = 0
for i in range(101):
    if i % 2 ==0:
        sum += i
print(sum)

# 使用python实现1~100之间的偶数求和
sum = 0
for i in range(2,101,2):
    sum += i
print(sum)

a = 1
while a == 1:
    print("a == 1")
    a += 1
else:
    print("a != 1")
    print(a)

# while循环 简单语句组
a = 1
while a ==1:a += 1
else:
    print("a != 1")
    print(a)

# break 和 continue的区别
for i in range(1,10):
    # 当 i 等于5时，终止这一轮的循环，5之后的print都不会再执行
    if i == 5:
        break
    print(i)

# continue
for i in range(1,10):
    # 当 i等于5时，会跳出这一次的循环，不执行print语句
    if i == 5:
        continue
    print(i)

# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机会根据人猜的数字分别给出提示 大一点 小一点 猜对了
import random

x = random.randint(1,100)

while True:
    y = int(input("请输入一个数字"))
    if y > x:
        print("小一点")
    elif y < x:
        print("大一点")
    elif y == x:
        print("猜对了")
        break
    