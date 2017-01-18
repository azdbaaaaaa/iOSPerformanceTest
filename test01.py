#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import sys
# import os
# import datetime
# import commands
import json

# aa = open("test.py").read()
# print type(aa)
with open("1.txt") as f:
    a = f.read()
    print json.loads(a)


# list1 = {"a": 1, "b": 2}

# b = json.dumps(list1)
# print type(b)
# print b
# c = json.loads(b)
# print type(c)
# print c

# with open("test.py") as s:
#     l = json.load(s)
# data = {
#     "name": 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
# print type(data)
# json_str = json.dumps(data)
# print json_str
# data = json.loads(json_str)
# print data
# dir_path = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# os.mkdir(dir_path)
# print dir_path
# InstrumentsTrace = sys.argv[1]
# # InstrumentsTrace = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/Instruments.trace"

# cmd = 'InstrumentsParser -p mmbang -i ' + InstrumentsTrace + ' -o ' + dir_path
# commands.getoutput(cmd)

# rootDir = sys.path[0]
# ActivityMonitorFile = rootDir + "/" + dir_path + "/ActivityMonitor-1"
# reportDemoFilePath = rootDir + "/" + "ReportDemo/ReportDemo.html"
# reportFilePath = rootDir + "/" + dir_path + "/Report.html"

# print ActivityMonitorFile
# print reportDemoFilePath
# print reportFilePath
# filename = '/Users/jimmy_zhou/Documents/iOSPerformanceTest/2016-07-27-11-40-06/ActivityMonitor-1'
# with open(filename).read() as s:
#     l = json.loads(s)


# filename = "/Users/jimmy_zhou/Documents/iOSPerformanceTest/1.txt"
# with open(filename) as s:
#     l = json.load(s)
#     print l


# json file:
# The file content of temp.json is:
# {
#  "name":"00_sample_case1",
#  "description":"an example."
# }
# file1 = "temp.json"
# f = open(file1)
# s = json.load(f)
# print s
# f.close

# json string:
# s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
# print s
# print s.keys()
# print s["name"]
# print s["type"]["name"]
# print s["type"]["parameter"][1]
