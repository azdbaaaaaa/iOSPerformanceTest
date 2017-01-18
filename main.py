#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import sys
import datetime
import commands
import json
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

dir_path = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
os.mkdir(dir_path)
# print dir_path
InstrumentsTrace = sys.argv[1]
# InstrumentsTrace = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/Instruments.trace"

rootDir = sys.path[0]
ActivityMonitorFile = rootDir + "/" + dir_path + "/ActivityMonitor-1"
CoreAnimationFile = rootDir + "/" + dir_path + "/CoreAnimation-1"
reportDemoFilePath = rootDir + "/" + "ReportDemo/ReportDemo.html"
reportFilePath = rootDir + "/" + dir_path + "/Report.html"
libPath = rootDir + "/lib"
InstrumentsParser = libPath + "/InstrumentsParser"

cmd = InstrumentsParser + ' -p mmbang -i ' + InstrumentsTrace + ' -o ' + dir_path
commands.getoutput(cmd)

# ActivityMonitor
with open(ActivityMonitorFile) as s:
    l = json.load(s)

VirtualSizeList = []
ResidentSizeList = []
DateList = []
CPUUsageList = []

for x in xrange(0, len(l)):
    Date = l[x]["Date"]
    VirtualSize = l[x]["VirtualSize"]
    ResidentSize = l[x]["ResidentSize"]
    CPUUsage = l[x]["CPUUsage"]

    DateList.append(Date.encode('utf-8'))
    VirtualSizeList.append(VirtualSize)
    ResidentSizeList.append(ResidentSize)
    CPUUsageList.append(CPUUsage)

MyDate = str(DateList)
memory_virtual_avg = sum(VirtualSizeList) / len(VirtualSizeList) / 1000 / 1000
memory_virtual_max = max(VirtualSizeList) / 1000 / 1000
memory_virtual_min = min(VirtualSizeList) / 1000 / 1000
memory_real_avg = sum(ResidentSizeList) / len(ResidentSizeList) / 1000 / 1000
memory_real_max = max(ResidentSizeList) / 1000 / 1000
memory_real_min = min(ResidentSizeList) / 1000 / 1000
cpu_avg = '%.2f%%' % (sum(CPUUsageList) / len(CPUUsageList))
cpu_max = '%.2f%%' % (max(CPUUsageList))
cpu_min = '%.2f%%' % (min(CPUUsageList))
MyVirtualSize = str(VirtualSizeList)
MyResidentSize = str(ResidentSizeList)
MyCPUUsage = str(CPUUsageList)

# CoreAnimation
with open(CoreAnimationFile) as s1:
    l1 = json.load(s1)

FramesDateList = []
FramesPerSecondList = []

for x in xrange(0, len(l1)):
    FramesDateStamp = l1[x]["XRVideoCardRunTimeStamp"]
    FramesDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(FramesDateStamp))
    FramesPerSecond = l1[x]["FramesPerSecond"]
    FramesDateList.append(FramesDate)
    FramesPerSecondList.append(FramesPerSecond)

MyFramesDate = str(FramesDateList)
MyFramesPerSecond = str(FramesPerSecondList)
fps_avg = sum(FramesPerSecondList) / len(FramesPerSecondList)
fps_max = max(FramesPerSecondList)
fps_min = min(FramesPerSecondList)

# ##########
# 渲染report
# ##########

with open(reportDemoFilePath, 'r+') as f:
    flist = f.readlines()
    flist[21] = MyDate + '\n'  # 22行：cpu使用率中的时间轴
    flist[52] = MyCPUUsage + '\n'  # 53行：cpu使用率中的cpu使用率值
    flist[76] = MyDate + '\n'  # 77行：memory中的时间轴
    flist[125] = MyVirtualSize + '\n'  # 126行：memory中的虚拟内存占用
    flist[127] = MyResidentSize + '\n'  # 128行：memory中的实际内存占用
    flist[153] = MyFramesDate + '\n'  # 154行：FPS时间轴
    flist[213] = MyFramesPerSecond + '\n'  # 214行：FPS值
    with open(reportFilePath, 'w+') as f2:
        f2.writelines(flist)

if reportFilePath is not None or reportFilePath is not "":
    try:
        html_doc = open(reportFilePath).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        soup.find(id="memory_virtual_avg").string = str(memory_virtual_avg)
        soup.find(id="memory_virtual_max").string = str(memory_virtual_max)
        soup.find(id="memory_virtual_min").string = str(memory_virtual_min)

        soup.find(id="memory_real_avg").string = str(memory_real_avg)
        soup.find(id="memory_real_max").string = str(memory_real_max)
        soup.find(id="memory_real_min").string = str(memory_real_min)

        soup.find(id="cpu_avg").string = str(cpu_avg)
        soup.find(id="cpu_max").string = str(cpu_max)
        soup.find(id="cpu_min").string = str(cpu_min)

        soup.find(id="fps_avg").string = str(fps_avg)
        soup.find(id="fps_max").string = str(fps_max)
        soup.find(id="fps_min").string = str(fps_min)
        with open(reportFilePath, 'w') as file:
            file.write(str(soup))

    except Exception, e:
        print("Exception:%s") % (e)
