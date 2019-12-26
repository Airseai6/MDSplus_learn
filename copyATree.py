# -*- coding:utf-8 -*-
# @Time   : 2019/12/25 19:02
# @Author : Qi

from MDSplus import Tree
from MDSplus import TreeNode
import time


def copy_tree(shot):
    tree_raw = Tree('exl50', shot)
    tree_cop = Tree('exl50_copy', shot, 'NEW')
    pools = ["AI", "FBC"]

    for pool in pools:
        nodes_list = []
        nodes_array = tree_raw.getNode(pool).getDescendants()
        nodes_list.extend(nodes_array)
        pool_nodes = [node.getNodeName() for node in nodes_list]

        tree_raw.setDefault(tree_raw.getNode(pool))
        tree_cop.setDefault(tree_cop.addNode(pool, "STRUCTURE"))
        for node in pool_nodes:
            tree_cop.addNode(node, "SIGNAL").addTags(node)
            # print(node)
            try:
                data = tree_raw.getNode(node).getData()
                tree_cop.getNode(node).putData(data)
                print(str(shot) + ':' + node)
            except Exception as e:
                pass
        tree_raw.setDefault(tree_raw.getNode("\EXL50::TOP"))
        tree_cop.setDefault(tree_cop.getNode("\EXL50_COPY::TOP"))

    tree_cop.write()


# def copy_tree2(shot):
#     tree_raw = Tree('exl50', shot)
#     tree_cop = Tree('exl50_copy', shot, 'NEW')
#     subtrees = ["AI", "FBC"]
#
#     for subtree in subtrees:
#         nodes = tree_raw.getNode(subtree).getNodeWild('***')
#         pool_nodes = nodes.getPath()
#
#         for node in pool_nodes:
#             tree_cop.addNode(node)
#             print(node)
#
#     tree_cop.write()


def cal_time(fun):
    def warper(*args, **kwargs):
        start_time = time.time()
        fun(*args, **kwargs)
        end_time = time.time()
        print("用时{}秒".format(end_time - start_time))
    return warper()


@cal_time
def main():
    copy_tree(-1)
    # copy_tree(-1)
    # for i in range(3601, 3604):
    #     print(i)
    #     copy_tree(i)


if __name__ == '__main__':
    main()
