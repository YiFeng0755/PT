#!/usr/bin/env python
#coding=utf-8

import pyecharts
import csv
import os

def cpuData(filePath):#返回cpu数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
        print("column:%s"%column)
    l=[]
    print("column:%s"%column[-1])
    if column[-1]==[]:
        for i in range(11, len(column) - 1):
            l.append(column[i][1].replace("%", ""))
    else:
        for i in range(11,len(column)):
            l.append(column[i][1])
    print(l)
    return l



def cpuChart(ymCpuPath,agCpuPath):
    cpuLine = pyecharts.Line("游密声网性能对比", "cpu(%)")
    ymCpu = cpuData(ymCpuPath)
    agCpu = cpuData(agCpuPath)
    cpuLine.add("游密", [x for x in range(len(ymCpu))], ymCpu, is_more_utils=True)  # 标题
    cpuLine.add("声网", [x for x in range(len(agCpu))], agCpu, is_more_utils=True)  # 标题
    cpuLine.show_config()  # 展示HTML源代码
    cpuLine.render("cpu.html")

def memData(filePath):#返回内存数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(12, len(column) - 1):
        l.append('%.2f'%(int(column[i][1])/1024))
    return l

def memChart(ymMemPath,agMemPath):
    memLine = pyecharts.Line("游密声网性能对比", "内存(Mb)")
    ymMem = memData(ymMemPath)
    agMem = memData(agMemPath)
    memLine.add("游密", [x for x in range(len(ymMem))], ymMem, is_more_utils=True)  # 标题
    memLine.add("声网", [x for x in range(len(agMem))], agMem, is_more_utils=True)  # 标题
    memLine.show_config()  # 展示HTML源代码
    memLine.render("mem.html")

def curData(filePath):#返回电流数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(11, len(column) - 1):
        l.append(column[i][1])
    return l

def curChart(ymCurPath,agCurPath):
    curLine = pyecharts.Line("游密声网性能对比", "电流(mA)")
    ymCur = curData(ymCurPath)
    agCur = curData(agCurPath)
    print(ymCur)
    print(agCur)
    curLine.add("游密", [x for x in range(len(ymCur))], ymCur, is_more_utils=True)  # 标题
    curLine.add("声网", [x for x in range(len(agCur))], agCur, is_more_utils=True)  # 标题
    curLine.show_config()  # 展示HTML源代码
    curLine.render("cur.html")

def netData(filePath):#返回流量数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    print(column)
    ltran = []#上行流量
    lrec = []#下行流量
    for i in range(12, len(column) - 1):
        ltran.append(column[i][1])
        lrec.append(column[i][2])
    return ltran,lrec

def netChart(ymNetPath,agNetPath):
    transLine = pyecharts.Line("游密声网性能对比", "transmit流量(KB)")
    recLine = pyecharts.Line("游密声网性能对比", "receive流量(KB)")
    ymTran,ymRec= netData(ymNetPath)
    agTran,agRec = netData(agNetPath)
    transLine.add("游密", [x for x in range(len(ymTran))], ymTran, is_more_utils=True)  # 标题
    transLine.add("声网", [x for x in range(len(agTran))], agTran, is_more_utils=True)  # 标题
    transLine.show_config()  # 展示HTML源代码
    transLine.render("Net_trans.html")

    recLine.add("游密", [x for x in range(len(ymRec))], ymRec, is_more_utils=True)  # 标题
    recLine.add("声网", [x for x in range(len(agRec))], agRec, is_more_utils=True)  # 标题
    recLine.show_config()  # 展示HTML源代码
    recLine.render("Net_rec.html")

def volData(filePath):#返回电压数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(11, len(column) - 1):
        l.append("%.2f"%(int(column[i][1])/1000))
    return l

def volChart(ymVolPath,agVolPath):
    volLine = pyecharts.Line("游密声网性能对比", "电压(V)")
    ymVol = volData(ymVolPath)
    agVol = volData(agVolPath)
    print(ymVol)
    print(agVol)
    volLine.add("游密", [x for x in range(len(ymVol))], ymVol, is_more_utils=True)  # 标题
    volLine.add("声网", [x for x in range(len(agVol))], agVol, is_more_utils=True)  # 标题
    volLine.show_config()  # 展示HTML源代码
    volLine.render("vol.html")

def genPath(ymCpuPath,agCpuPath):
    ymPath = ymCpuPath.replace(ymCpuPath.split(os.sep)[-1], "")
    agPath = agCpuPath.replace(agCpuPath.split(os.sep)[-1], "")
    # 获取ym内存数据文件路径
    ymMemCmd = 'dir {} |find "{}"|gawk "{}"'.format(ymPath,"Ps","NR==1{print $4}")
    ymMemFileName = os.popen(ymMemCmd).read()
    ymMemPath = os.path.join(ymPath,ymMemFileName).strip()

    # 获取ag内存数据文件路径
    agMemCmd = 'dir {} |find "{}"|gawk "{}"'.format(agPath, "Ps", "NR==1{print $4}")
    agMemFileName = os.popen(agMemCmd).read()
    agMemPath = os.path.join(agPath, agMemFileName).strip()

    # 获取ym电流数据文件路径
    ymCurCmd = 'dir {} |find "{}"|gawk "{}"'.format(ymPath, "Cur", "NR==1{print $4}")
    ymCurFileName = os.popen(ymCurCmd).read()
    ymCurPath = os.path.join(ymPath, ymCurFileName).strip()

    # 获取ag电流数据文件路径
    agCurCmd = 'dir {} |find "{}"|gawk "{}"'.format(agPath, "Cur", "NR==1{print $4}")
    agCurFileName = os.popen(agCurCmd).read()
    agCurPath = os.path.join(agPath, agCurFileName).strip()

    # 获取ym流量数据文件路径
    ymNetCmd = 'dir {} |find "{}"|gawk "{}"'.format(ymPath, "NET", "NR==1{print $4}")
    ymNetFileName = os.popen(ymNetCmd).read()
    ymNetPath = os.path.join(ymPath, ymNetFileName).strip()

    # 获取ag流量数据文件路径
    agNetCmd = 'dir {} |find "{}"|gawk "{}"'.format(agPath, "NET", "NR==1{print $4}")
    agNetFileName = os.popen(agNetCmd).read()
    agNetPath = os.path.join(agPath, agNetFileName).strip()

    # 获取ym电压数据文件路径
    ymVolCmd = 'dir {} |find "{}"|gawk "{}"'.format(ymPath, "Volt", "NR==1{print $4}")
    ymVolFileName = os.popen(ymVolCmd).read()
    ymVolPath = os.path.join(ymPath, ymVolFileName).strip()

    # 获取ag电压数据文件路径
    agVolCmd = 'dir {} |find "{}"|gawk "{}"'.format(agPath, "Volt", "NR==1{print $4}")
    agVolFileName = os.popen(agVolCmd).read()
    agVolPath = os.path.join(agPath, agVolFileName).strip()


    return ymMemPath,agMemPath,ymCurPath,agCurPath,ymNetPath,agNetPath,ymVolPath,agVolPath

if __name__ == "__main__":
    ymCpuPath = input("拖入游密cpu文件: ")
    agCpuPath = input("拖入声网cpu文件：")
    ymMemPath,agMemPath,ymCurPath,agCurPath,ymNetPath,agNetPath,ymVolPath,agVolPath = genPath(ymCpuPath,agCpuPath)
    cpuChart(ymCpuPath,agCpuPath)
    memChart(ymMemPath, agMemPath)
    curChart(ymCurPath,agCurPath)
    netChart(ymNetPath,agNetPath)
    volChart(ymVolPath, agVolPath)
    # filePath = "D:\PycharmProjects\\PT\perTest\CPU_20190202213507.csv"
    # filePath2 = "D:\ChromeDownloads\GW\im.youme.talk.sample\\1.0\\123\CPU_20190125201625.csv"
    # cpuData(filePath)
    # cpuData(filePath2)