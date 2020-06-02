str = "my name is lili"
print(str)

# 格式化输出
str1 = "my age is %d" %20
print(str1)

name = "Tom"
str = "my name is %s,my age is %d"%(name,20)
print(str)

print("PI = %.2f"%3.1415)

# format方法
name1 = "Tom"
name2 = "Jerry"
print("tow boy are {} and {}".format(name1,name2))
print("two boy are {0} and {1},{0} is Tom,{1} is Jerry".format(name1,name2))

dic = {"name":"Tom","age":"20"}
print("my name is {name} my age is {age}".format(**dic))

#F-strings方法，不可以在大括号中加反斜杠
name = 'ERIC'
print(f'my name is {name}')
print(f'my name is {name.lower()}')
print(f'1 + 1 = {1+1}')

f = open("inputtest.json")
print(f.readline())
# print(f.read())

print(f.readable())
# 以列表形式打印
print(f.readlines())
f.close()

# 使用with这种方式可以不需要关闭文件流，会自动关闭
with open('inputtest.json') as f:
    print(f.readlines())


with open('inputtest.json') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break

#JSON
import json
info = [{
    "name":"Tom",
    "gender":"male",
    "other":None},{
    "name":"Jack",
    "gender":"male",
    "other":None
    }]

data = json.dumps(info,sort_keys=True,indent=4)
print(data)
print(type(data))

#JSON dump 把数据类型转换成字符串并存储在文件中
info = [{
    "name":"Tome",
    "gender":"male",
    "other":None
},{
    "name":"Jack",
    "gender":"male",
    "other":None
}]
print("读取json文件")
json.dump(info,open("inputtest.json","w"))

#JSON load 将字符串转换为json
str2 = '''
[{
    "name":"Tom",
    "gender":"male"
},{
    "name":"Jack",
    "gender":"male"
}]
'''
print(type(str2))
data = json.loads(str2)
print(type(data))
print(data)

# JSON load把文件打开从字符串转换成json
jsObj = json.load(open('inputtest.json','r'))
print(jsObj)
print(type(jsObj))
print(jsObj[0]['name'])