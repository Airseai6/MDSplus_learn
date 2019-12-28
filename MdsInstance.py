# -*- coding:utf-8 -*-
# @Time   : 2019/12/27 8:20
# @Author : Qi

# --------------------------- Tree Methods ---------------------------
from MDSplus import Tree
t = Tree('my_tree', -1)
# ----------------------- Instance Methods -----------------------
dfs = t.getDatafileSize()
# t.cleanDatafile()
# t.compressDatafile()
fn = t.getFileName()
t2 = t.copy()
# t.close()
# top = t.top()
# ad = t.addDevice('SUB3')
# an = t.addNode('SUB4')
# createPulse(1)
dir = t.dir()
# gc = t.getCurrent('SUB1')
gd = t.getDefault()
gn = t.getNode("SUB1")
gnwi_iterator = t.getNodeWildIter('***')
gnw_array = t.getNodeWild('***')
gtc_tuple = t.getTimeContext()
im_bool = t.isModified()
# sd_tn = t.setDefault("SUB1")

# ----------------------- Static  Methods -----------------------
# gvd_str = t.getVersionDate()
# --------------------------- TreeNode Methods ---------------------------
# from MDSplus import TreeNode
tn = t.getNode("SUB1")
c_tn = tn.copy()
opn_str = tn.ORIGINAL_PART_NAME()
pn_str = tn.PART_NAME()
# cn = tn.children_nids()
# mn = tn.member_nids()
# desc = tn.descendants()
# nod_i = tn.number_of_descendants()g
# ic_bool = tn.is_child()
# nid_n = tn.nid_number()
gb_tn = tn.getBrother()
gc_tn = tn.getChild()
gc_tnarr = tn.getChildren()
gc_str = tn.getClass()
print('used to pause!')