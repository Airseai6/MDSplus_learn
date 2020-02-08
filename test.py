#! python3
# -*- coding:utf-8 -*-

from MDSplus import Tree
from MDSplus import TreeNode

t = Tree('my_tree', -1)
node_str = "SUB1"
node1 = t.getNode(node_str)
node_path = node1.getMinPath()
node_path2 = node1.getPath()
node_path3 = node1.getFullPath()
node_name = node1.getNodeName()
node_father = node1.getParent()
node_dtype = node1.getDtype()
node_att = node1.getExtendedAttribute('NUMERIC')  # ??
node_nid = node1.getNid()
child_num = node1.getNumChildren()
child_num2 = node1.getNumDescendants()
print(11)

