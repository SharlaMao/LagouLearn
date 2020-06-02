import os

# os.mkdir("testdir")
# os.removedirs("testdir")

print(os.listdir("./"))

print(os.getcwd())

print(os.path.exists("testdir"))

if not os.path.exists("testdir"):
    os.mkdir("testdir")
if not os.path.exists("testdir/test.txt"):
    f = open("testdir/test.txt","w")
    f.write("hello,os using")
    f.close()

import time

print(time.asctime())
print(time.time())
print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 报错
# print(time.strftime("%Y年%m月%d日  %H:%M:%S",time.localtime()))

# 获取三天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
print(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime(two_day_before)))

# 获取两天后的时间
now_timestamp = time.time()
two_day_after = now_timestamp + 60*60*24*2
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(two_day_after)))

import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.read())