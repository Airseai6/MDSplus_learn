# -*- coding:utf-8 -*-
# @CreateTime : 2020/2/8 17:29
# @Author     : Qi

from MDSplus import Tree


def getChannelDic(tree, ):
    # 获取节点列表
    subtrees = ['AI', 'FBC',]
    channel_dic = {}
    for subtree in subtrees:
        nodes_array = tree.getNode(subtree).getDescendants()
        nodes_name = [node.getNodeName() for node in nodes_array]
        channel_dic[subtree] = nodes_name
    return channel_dic


def getData(tree, channel_name):
    data = tree.getNode(channel_name).data()
    data_list = [item for item in data]
    return data_list


if __name__ == '__main__':
    tree = Tree('exl50_copy', 3602,)
    cha_name = getChannelDic(tree)
    cha_len = {}
    for k, v in cha_name.items():
        for item in v:
            channel = k + ':' + item
            print(channel)