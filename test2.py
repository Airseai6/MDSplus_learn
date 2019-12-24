# -*- coding:utf-8 -*-
# @Time   : 2019/12/24 8:33
# @Author : Qi

from MDSplus import *

t = Tree('exl50', -1)
node1 = t.getNode("AI")
# node1 = t.getNode("FBC")
d1 = node1.getNodeWild('***')
# print(d1)
print(d1.getPath())

