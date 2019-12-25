# -*- coding:utf-8 -*-
# @Time   : 2019/12/25 19:02
# @Author : Qi

from MDSplus import Tree


def copy_tree(shot):
    tree_raw = Tree('exl50', shot)
    tree_cop = Tree('exl50_copy', shot, 'NEW')

    subtrees = ["AI", "FBC"]

    nodes_name_list = []
    for subtree in subtrees:

        nodes = tree_raw.getNode(subtree).getDescendants()
        nodes_name_list.extend(nodes)
        pool_nodes = [x.getNodeName() for x in nodes_name_list]

        tree_cop.setDefault(tree_cop.addNode(subtree, "STRUCTURE"))
        for node in pool_nodes:
            tree_cop.addNode(node)
            print(node)

    tree_cop.write()


def copy_tree2(shot):
    tree_raw = Tree('exl50', shot)
    tree_cop = Tree('exl50_copy', shot, 'NEW')
    subtrees = ["AI", "FBC"]

    for subtree in subtrees:
        nodes = tree_raw.getNode(subtree).getNodeWild('***')
        pool_nodes = nodes.getPath()

        for node in pool_nodes:
            tree_cop.addNode(node)
            print(node)

    tree_cop.write()


if __name__ == '__main__':
    copy_tree(-1)
