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
    print(len(d1.getPath()))
    print(x.getNodeName() for x in d1.getPath())
    print(len(d2.getPath()))


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


if __name__ == '__main__':
    main()
    print(len(get_nodes_name(-1)))
    print(get_nodes_name(-1))

