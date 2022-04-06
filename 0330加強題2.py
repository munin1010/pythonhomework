# -*- coding: utf-8 -*-
"""
有3個數字組成多少個不重複的數字
"""

for i in range(10):
    for x in range(10):
        for t in range(10):
            print("%d%d%d"%(i,x,t),end=",")
        