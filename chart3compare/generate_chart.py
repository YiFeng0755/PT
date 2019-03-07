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



def cpuChart(ymCpuPath,qqCpuPath,xyCpuPath):
    cpuLine = pyecharts.Line("游密、qq、小鱼性能对比", "cpu(%)")
    ymCpu = cpuData(ymCpuPath)
    qqCpu = cpuData(qqCpuPath)
    xyCpu = cpuData(xyCpuPath)
    cpuLine.add("游密", [x for x in range(len(ymCpu))], ymCpu, is_more_utils=True)  # 标题
    cpuLine.add("qq", [x for x in range(len(qqCpu))], qqCpu, is_more_utils=True)  # 标题
    cpuLine.add("小鱼", [x for x in range(len(xyCpu))], xyCpu, is_more_utils=True)  # 标题
    # cpuLine.show_config()  # 展示HTML源代码
    cpuLine.render("cpu.html")

def memData(filePath):#返回内存数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(12, len(column) - 1):
        l.append('%.2f'%(int(column[i][1])/1024))
    return l

def memChart(ymMemPath,qqMemPath,xyMemPath):
    memLine = pyecharts.Line("游密、qq、小鱼性能对比", "内存(MB)")
    ymMem = memData(ymMemPath)
    qqMem = memData(qqMemPath)
    xyMem = memData(xyMemPath)
    memLine.add("游密", [x for x in range(len(ymMem))], ymMem, is_more_utils=True)  # 标题
    memLine.add("qq", [x for x in range(len(qqMem))], qqMem, is_more_utils=True)  # 标题
    memLine.add("小鱼", [x for x in range(len(xyMem))], xyMem, is_more_utils=True)  # 标题
    # memLine.show_config()  # 展示HTML源代码
    memLine.render("mem.html")

def curData(filePath):#返回电流数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(11, len(column) - 1):
        l.append(column[i][1])
    return l

def curChart(ymCurPath,qqCurPath,xyCurPath):
    curLine = pyecharts.Line("游密、qq、小鱼性能对比", "电流(mA)")
    ymCur = curData(ymCurPath)
    qqCur = curData(qqCurPath)
    xyCur = curData(xyCurPath)
    curLine.add("游密", [x for x in range(len(ymCur))], ymCur, is_more_utils=True)  # 标题
    curLine.add("qq", [x for x in range(len(qqCur))], qqCur, is_more_utils=True)  # 标题
    curLine.add("xy", [x for x in range(len(xyCur))], xyCur, is_more_utils=True)  # 标题
    # curLine.show_config()  # 展示HTML源代码
    curLine.render("cur.html")

def netData(filePath):#返回流量数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    # print(column)
    ltran = []#上行流量
    lrec = []#下行流量
    brtran = []#上行码率
    brrec = []#下行码率
    for i in range(12, len(column) - 1):
        ltran.append(column[i][1])
        lrec.append(column[i][2])
        if i<len(column) - 2:
            brtran.append(int(column[i+1][1])-int(column[i][1]))
            brrec.append(int(column[i + 1][2]) - int(column[i][2]))
    return ltran,lrec,brtran,brrec

def netChart(ymNetPath,qqNetPath,xyNetPath):
    transLine = pyecharts.Line("游密、qq、小鱼性能对比", "transmit流量(KB)")
    recLine = pyecharts.Line("游密、qq、小鱼性能对比", "receive流量(KB)")
    ymTran,ymRec,ymbtran,ymbrec= netData(ymNetPath)
    qqTran,qqRec,qqbtran,qqbrec = netData(qqNetPath)
    xyTran,xyRec,xybtran,xybrec = netData(xyNetPath)
    transLine.add("游密", [x for x in range(len(ymTran))], ymTran, is_more_utils=True)  # 标题
    transLine.add("qq", [x for x in range(len(qqTran))], qqTran, is_more_utils=True)  # 标题
    transLine.add("小鱼", [x for x in range(len(xyTran))], xyTran, is_more_utils=True)  # 标题
    # transLine.show_config()  # 展示HTML源代码
    transLine.render("Net_trans.html")

    recLine.add("游密", [x for x in range(len(ymRec))], ymRec, is_more_utils=True)  # 标题
    recLine.add("qq", [x for x in range(len(qqRec))], qqRec, is_more_utils=True)  # 标题
    recLine.add("小鱼", [x for x in range(len(xyRec))], xyRec, is_more_utils=True)  # 标题
    # recLine.show_config()  # 展示HTML源代码
    recLine.render("Net_rec.html")

    btranLine = pyecharts.Line("游密、qq、小鱼性能对比", "上行带宽码率(KB/s)")
    brecLine = pyecharts.Line("游密、qq、小鱼性能对比", "下行带宽码率(KB/s)")
    btranLine.add("游密", [x for x in range(len(ymbtran))], ymbtran, is_more_utils=True)  # 标题
    btranLine.add("qq", [x for x in range(len(qqbtran))], qqbtran, is_more_utils=True)  # 标题
    btranLine.add("小鱼", [x for x in range(len(xybtran))], xybtran, is_more_utils=True)  # 标题
    # btranLine.show_config()  # 展示HTML源代码
    btranLine.render("br_trans.html")

    brecLine.add("游密", [x for x in range(len(ymbrec))], ymbrec, is_more_utils=True)  # 标题
    brecLine.add("qq", [x for x in range(len(qqbrec))], qqbrec, is_more_utils=True)  # 标题
    brecLine.add("小鱼", [x for x in range(len(xybrec))], xybrec, is_more_utils=True)  # 标题
    # brecLine.show_config()  # 展示HTML源代码
    brecLine.render("br_rec.html")



def volData(filePath):#返回电压数据列表
    with open(filePath,"rt")as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
    l=[]
    for i in range(11, len(column) - 1):
        l.append("%.2f"%(int(column[i][1])/1000))
    return l

def volChart(ymVolPath,qqVolPath,xyVolPath):
    volLine = pyecharts.Line("游密、qq、小鱼性能对比", "电压(V)")
    ymVol = volData(ymVolPath)
    qqVol = volData(qqVolPath)
    xyVol = volData(xyVolPath)
    volLine.add("游密", [x for x in range(len(ymVol))], ymVol, is_more_utils=True)  # 标题
    volLine.add("qq", [x for x in range(len(qqVol))], qqVol, is_more_utils=True)  # 标题
    volLine.add("小鱼", [x for x in range(len(xyVol))], xyVol, is_more_utils=True)  # 标题
    # volLine.show_config()  # 展示HTML源代码
    volLine.render("vol.html")

def genPath(CpuPath):
    filePath = CpuPath.replace(CpuPath.split(os.sep)[-1], "")

    # 获取内存数据文件路径
    MemCmd = 'dir {} |find "{}"|gawk "{}"'.format(filePath,"Ps","NR==1{print $4}")
    MemFileName = os.popen(MemCmd).read()
    MemPath = os.path.join(filePath,MemFileName).strip()

    # 获取电流数据文件路径
    CurCmd = 'dir {} |find "{}"|gawk "{}"'.format(filePath, "Cur", "NR==1{print $4}")
    CurFileName = os.popen(CurCmd).read()
    CurPath = os.path.join(filePath,CurFileName).strip()

    # 获取流量数据文件路径
    NetCmd = 'dir {} |find "{}"|gawk "{}"'.format(filePath, "NET", "NR==1{print $4}")
    NetFileName = os.popen(NetCmd).read()
    NetPath = os.path.join(filePath, NetFileName).strip()

    # 获取电压数据文件路径
    VolCmd = 'dir {} |find "{}"|gawk "{}"'.format(filePath, "Volt", "NR==1{print $4}")
    VolFileName = os.popen(VolCmd).read()
    VolPath = os.path.join(filePath,VolFileName).strip()
    return MemPath,CurPath,NetPath,VolPath

if __name__ == "__main__":
    ymCpuPath = input("拖入游密cpu文件: ")
    qqCpuPath = input("拖入QQcpu文件：")
    xyCpuPath = input("拖入小鱼cpu文件：")
    ymMemPath,ymCurPath,ymNetPath,ymVolPath = genPath(ymCpuPath)
    qqMemPath,qqCurPath,qqNetPath,qqVolPath = genPath(qqCpuPath)
    xyMemPath,xyCurPath,xyNetPath,xyVolPath = genPath(xyCpuPath)
    # cpuChart(ymCpuPath,qqCpuPath,xyCpuPath)
    # memChart(ymMemPath,qqMemPath,xyMemPath)
    # curChart(ymCurPath,qqCurPath,xyCurPath)
    netChart(ymNetPath,qqNetPath,xyNetPath)
    # volChart(ymVolPath,qqVolPath,xyVolPath)
    # filePath = "D:\PycharmProjects\\PT\perTest\CPU_20190202213507.csv"
    # filePath2 = "D:\ChromeDownloads\GW\im.youme.talk.sample\\1.0\\123\CPU_20190125201625.csv"
    # cpuData(filePath)
    # cpuData(filePath2)