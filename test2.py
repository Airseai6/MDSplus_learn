# -*- coding:utf-8 -*-
# @Time   : 2019/12/24 8:33
# @Author : Qi

from MDSplus import *


def main():
    t = Tree('exl50', -1)
    node1 = t.getNode("AI")
    node2 = t.getNode("FBC")
    d1 = node1.getNodeWild('***')
    d2 = node2.getNodeWild('***')
    print(x.getNodeName() for x in d1.getPath())
    print(d1.getPath())


def get_nodes_name(shot):
    subtrees = ["AI", "FBC"]
    nodes_name_list = []
    t = Tree("exl50", shot)
    for subtree in subtrees:
        nodes = t.getNode(subtree)
        nodes_d = nodes.getDescendants()
        nodes_name_list.extend(nodes_d)
        pool = []
        for node_name in nodes_name_list:
            pool.append(node_name.getNodeName)
    return pool


def write_tree():
    tree = Tree('my_tree', -1, 'NEW')
    tree.addNode(":NUM1", "NUMERIC")
    tree.addNode(":NUM2", "NUMERIC")
    tree.addNode(":NUM3", "NUMERIC")
    tree.addNode(":TXT", "TEXT")
    tree.setDefault(tree.addNode(".SUB1", "STRUCTURE"))
    tree.addNode(":SUB_NODE1", "NUMERIC")
    tree.addNode(".SUB2", "STRUCTURE")
    tree.addNode(".SUB2:SUB_NODE2", "NUMERIC").addTag("TAG1")
    tree.write()


if __name__ == '__main__':
    main()

