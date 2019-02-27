#!/usr/bin/env python
#coding:utf-8
import os,re,time,csv
import multiprocessing.pool
import selectors,asyncio
#python2可以用file替代open
# with open("D:\\PycharmProjects\\PT\\perTest\\CPU_20190202211323.csv","w",newline='') as csvfile:
#     writer = csv.writer(csvfile)
#
#     #先写入columns_name
#     # writer.writerow(["index","a_name","b_name"])
#     #写入多行用writerows
#     writer.writerows([['key', 'CPU'], ['alias', 'CPU'], ['unit', '(%)'], ['begin date', '2019/02/02'], ['end date', '2019/02/02'], ['count', 9], ['', ''], ['min', 3.77], ['max', 8.18], ['avg', '5.86'], ['', ''], ['21:13:12', '7.53'], ['21:13:14', '3.77'], ['21:13:15', '6.45'], ['21:13:16', '5.75'], ['21:13:17', '4.68'], ['21:13:19', '8.18'], ['21:13:20', '5.30'], ['21:13:21', '4.04'], ['21:13:22', '7.06']])
# def gen():
#     yield 1
#     html = yield "www.baidu.com"
#     print(html)
#
# if __name__ == "__main__":
#     g = gen()
#     print(g.send(None))
#     print(g.send(2))

# def h():
#     print('Wen Chuan',)
#     m = yield 5  # Fighting!
#     print(m)
#     # print(None)
#     d = yield 12
#     print('We are together!')
# c = h()
# next(c)  #相当于c.send(None)
# next(c)
# # # c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'
# next(c)

def h():
    total = 0
    while True:
        x=yield
        print(x)
        if not x:
            break
        total +=x
    return total

if __name__ == "__main__":
    g= h()
    g.send(None)
    g.send(1)
    g.send(2)
    g.send(3)
    try:
        g.send(None)
    except Exception as e:
        print(e.value)

t = ["x" for i in range(10)]
print(t)

import asyncio
asyncio.gather()
loop = asyncio.new_event_loop()
loop.run_until_complete
