#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import os
# import time
import sys
import json
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


filename = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/ActivityMonitor-1"
reportDemoFilePath = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/ReportDemo.html"
reportFilePath = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/Report.html"

with open(filename).read() as s:
    l = json.loads(s)

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

    # DateTemp = "'" + Date + "',"
    # VirtualSizeTemp = "%s," % VirtualSize
    # ResidentSizeTemp = "%s," % ResidentSize
    # CPUUsageTemp = "%s," % CPUUsage

    # MyDate = MyDate + DateTemp
    # MyVirtualSize = MyVirtualSize + VirtualSizeTemp
    # MyResidentSize = MyResidentSize + ResidentSizeTemp
    # MyCPUUsage = MyCPUUsage + CPUUsageTemp

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
# print MyDate
# print MyResidentSize
# print MyVirtualSize
# print MyCPUUsage

# ##########
# 渲染report
#
#
# ##########



with open(reportDemoFilePath, 'r+') as f:
    flist = f.readlines()
    flist[21] = MyDate + '\n'  # 22行：cpu使用率中的时间轴
    flist[52] = MyCPUUsage + '\n'  # 53行：cpu使用率中的cpu使用率值
    flist[76] = MyDate + '\n'  # 77行：memory中的时间轴
    flist[125] = MyVirtualSize + '\n'  # 126行：memory中的虚拟内存占用
    flist[127] = MyResidentSize + '\n'  # 128行：memory中的实际内存占用
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
        with open(reportFilePath, 'w') as file:
            file.write(str(soup))

    except Exception, e:
        print("Exception:%s") % (e)
