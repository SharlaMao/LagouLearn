list1 = [1,5,3,6,5]
# 在列表的末尾添加一个元素
list1.append(0)
print("list Of append:",list1)
# 在给定的位置添加一个元素
list1.insert(1,0)
print("list Of insert(1,0):",list1)
# remove 删除 找到元素值，而不是根据索引删除
list1.remove(1)
print("list of remove:",list1)
# pop 删除 根据索引删除，和remove相区分 还有返回值
y = list1.pop(0);
print("list Of pop:",list1)
print("pop Of return:",y)
# sort 升序排序
list1.sort()
print(list1)
# 降序排序
list1.sort(reverse=True)
print(list1)
# 反转当前排序
list1.reverse()
print(list1)

# 列表推导式，生成一个平方列表
list2 = []
for i in range(4):
    list2.append(i**2)
print(list2)

# 列表推导式
list3 = [i**2 for i in range(1,4)]
print(list3)

list4 = []
for i in range(1,4):
    if i != 1:
        list4.append(i**2)
print(list4)

list5 = [i**2 for i in range(1,4) if i !=1 ]

list6 = []
for i in range(1,4):
    for j in range(1,4):
        list6.append(i*j)
print(list6)

list7 = [i*j for i in range(1,4) for j in range(1,4) ]
print(list7)

# 元组
tuple1 = (1,2,3,1,1,1)
tuple2  = "a",
print(tuple1)
print(tuple2)
print(tuple1[0])
# 元组的内置函数的使用
print(tuple1.index(1))
# 查找1出现了几次 
print(tuple1.count(1))
# 元组和列表谁占的内存空间比较大,列表大
tuple3 = []
list8 = []
import sys
sys.getsizeof(tuple3)
sys.getsizeof(list8)
# 如何改变元组
tuple4 = ([1,2,3],2,3)

tuple4[0][0] = "aaaa"
print(tuple4)

c1 = {"a","b","c","d","e","e"}
print(c1)

# set函数的用途1：定义一个空集合
c2 = set({""})
print(c2)

# set函数的用途2：去重
c3 = set("aaaaaaaaaa")
print(c3)

# 集合使用列表推导式
c4 = {i for i in "aaaaaaaaaa"}
print(c4)

# 如何定义字典
# 不能使用列表作为key d1 = {[]:1}
d1 = {"a":1,"b":2}
print(d1)
d2 = dict(a=1,b=2)
print(d2)

# 字典的方法
y = d1.pop("a")
print(d1)
# pop的返回值，是该键的键值
print(y)
print(d2.keys())
print(d2.values())

# 字典定义 使用推导式
d4 = {i:i*2 for i in range(1,4)}
print(d4)