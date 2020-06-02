def method(a,b=[]):
    """

    :param a:
    :return:
    """
    b.append(a)
    return b

print(method(1))
print(method(2))

# 参数为字典形式
def method1(**a):
    print(a.keys())

method1(a=1,b=2,c=3)

# 元组传参
def method2(*a):
    print(a[0])
    print(a[1])
    print(a[2])

method2(1,2,3)

# lambda
y = lambda x:x*2
y1 = lambda x,y,z:x+y+z

print(y(2))
print(y1(1,2,3))