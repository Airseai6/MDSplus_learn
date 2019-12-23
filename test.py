#! python3
# -*- coding:utf-8 -*-
from MDSplus import *


t = Tree("my_tree", -1)
node1 = t.getNode("NUM3")
node2 = t.getNode("SUB2")
print(node1)
print(node2)
d1 = node1.getData()
d2 = node2.getNodeWild('***')
print(d1)
print(d2.getPath())

