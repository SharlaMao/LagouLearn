print("hello pycharm")
print("hello pycharm")

# a = 1
# b = 2
a,b = 1,2
print(a)
print(b)

int_a = 1
float_a = 2.1
complex_a = 2j

print(type(int_a))
print(type(float_a))
print(type(complex_a))

string_a = "string\\n";
print(string_a)

string_aa = "aaaaaaaa"
string_bb = "bbbbbbbb"
print(string_aa+string_bb)
print("string_aa" "string_bb")

string_cc = f"bbbbbbbb{string_aa}"
print(string_cc)

string_dd = "ddddddddd{}{}"
print(string_dd.format(string_aa,string_bb))

string_dd = "ddddddddd{x}{y}"
print(string_dd.format(x=string_aa,y=string_bb))

list_a = [1,2,3,"a","b"]
print(list_a[0])
print(list_a[-1])

print(list_a[0:3])


f = 1;
if f ==0:
    print("f=0")
elif f == 1:
    print("f = 1")
elif f == 2:
    print(" f = 2")
else:
    print("a 不等于 0、1、2")

# 分别使用分支嵌套以及多重分支去实现分段函数求值
x = -2
# 多重分支
if x > 1:
    print(3*x-5)
elif x >= -1:
    print(x+2)
elif x < -1:
    print(5*x+3)

# 分支结构
if x > 1:
    print(3*x-5)
else:
    if x >= -1:
        print(x+2)
    else:
        print(5*x+3)

