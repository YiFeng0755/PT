#!/usr/bin/env python
#coding:utf-8
import os,re,time,csv

def pID(pkgName):
    cmd = 'adb shell ps -A|findstr "{}"'.format(pkgName)
    out = os.popen(cmd).read()
    ol=re.split("\s+",out)
    pid =ol[1]
    return pid

def getTotalCpuTime():
    cmd = 'adb shell cat /proc/stat'
    out = os.popen(cmd).read()
    cpuLine = out.split("\n")[0]
    tl = re.split("\s+",cpuLine)
    tt = 0
    for i in range(1,len(tl)):
        tt += int(tl[i])
    return tt

def getAppCpuTime(pid):
    cmd = 'adb shell cat /proc/{}/stat'.format(pid)
    out = os.popen(cmd).read()
    l = re.split("\s+",out)
    print(l)
    act = int(l[13])+int(l[14])+int(l[15])+int(l[16])
    return act

def getKernelNum():
    cmd = 'adb shell cat /proc/stat'
    out =os.popen(cmd).read()
    l = out.split("\n")
    n = -1
    for el in l:
        if "cpu" in el:
            n+=1
    return n

def calPercent(pkgName,sp_itv=0.001):
    pid = pID(pkgName)
    print("pid:%s"%pid)
    kn = getKernelNum()
    print("kn:%s" % kn)
    o_tcpu = getTotalCpuTime()
    print("o_tcpu:%s"%o_tcpu)
    o_acpu = getAppCpuTime(pid)
    print("o_acpu:%s"%o_acpu)
    # c_tcpu = o_tcpu
    # c_acpu = o_acpu
    while True:
        time.sleep(sp_itv)
        c_tcpu = getTotalCpuTime()
        print("c_tcpu:%s" % c_tcpu)
        c_acpu = getAppCpuTime(pid)
        print("c_acpu:%s" % c_acpu)
        if(c_tcpu!=o_tcpu & c_acpu!=o_acpu):
            break
    pt ="%.2f" %(100*(c_acpu-o_acpu)/(c_tcpu-o_tcpu))
    print("pt:%s"%pt)
    return pt

def dataLen():
    filePath = input("请拖入cpu文件:")
    with open(filePath,"rt",newline='')as csvfile:
        reader = csv.reader(csvfile)
        column = [row for row in reader]
        print(column)
    return len(column)

def initCsvFile():
    dirPath = os.getcwd()
    tt = time.strftime("%Y%m%d%H%M%S")
    filePath=dirPath+os.sep+"CPU_"+tt+".csv"
    print(filePath)
    # Path2=r"\\".join(Path1.split("\\"))
    cmd = "type nul>"+filePath
    os.popen(cmd)
    return filePath

def startSample(st=600,pkgName="im.youme.talk.sample"):
    bt = time.time()
    dataList = []
    while True:
        l=[]
        t=time.strftime("%H:%M:%S")
        l.append(t)
        pt=calPercent(pkgName)
        l.append(pt)
        dataList.append(l)
        ct=time.time()
        if (ct-bt>st):
            break
    print(dataList)
    return dataList

def write2csv(datalist,filePath):
    dt =time.strftime("%Y/%m/%d")
    print("dt:%s"%dt)
    print("filepath:%s"%filePath)
    l1 = ["key","CPU"]
    l2 = ["alias","CPU"]
    l3 = ["unit","(%)"]
    l4 = ["begin date"]
    l4.append(dt)
    print ("l4:%s"%l4)
    l5 = ["end date"]
    l5.append(dt)
    print("l5:%s" % l5)
    l6 = ["count"]
    l6.append((len(datalist)))
    print("l6:%s" % l6)
    l7 = ["",""]
    ptList = []
    for data in datalist:
        ptList.append(float(data[1]))
    mx = max(ptList)
    mi = min(ptList)
    avg = '%.2f'%(sum(ptList)/len(ptList))
    l8 = ["min",mi]
    l9 = ["max",mx]
    l10 = ["avg",avg]
    l11 = ["",""]
    l =[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11]
    for data in datalist:
        l.append(data)
    print(l)
    with open(filePath,"w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(l)

if __name__ == "__main__":
    # a =pID("im.youme.talk.sample")
    # print(a)
    # b= getAppCpuTime("2739")
    # c=getKernelNum()
    # calPercent("im.youme.talk.sample")
    # filePath ="C:\\Users\\aa\\Desktop\\CPU_20190125202814.csv"
    # with open(filePath,"rt",newline='')as csvfile:
    #     reader = csv.reader(csvfile)
    #     column = [row for row in reader]
    # print(column)
    # dataLen()
    # initCsvFile()
    # datalist = startSample(pkgName="im.youme.video.sample2")
    datalist = startSample(pkgName="com.tencent.mobileqq")
    # datalist = startSample(pkgName="com.ainemo.dragoon")
    filePath = initCsvFile()
    print(filePath)
    time.sleep(2)
    write2csv(datalist,filePath)