# -*- coding:utf-8 -*-
# @CreateTime : 2020/2/8 17:29
# @Author     : Qi

from MDSplus import Tree

class mdsTree():
    def __init__(self, dbname, shot, ):
        self.tree = Tree(dbname, shot)

        # 节点列表 {'AI':[...], 'FBC':[...]}
        subtrees = ['AI', 'FBC',]
        self.channel_dic = {}
        for subtree in subtrees:
            nodes_array = self.tree.getNode(subtree).getDescendants()
            nodes_name = [node.getNodeName() for node in nodes_array]
            self.channel_dic[subtree] = nodes_name

    def close(self):
        self.tree.close

    def getCurrentShot(self):
        try:
            shot_num = self.tree.getCurrent()
        except Exception as e:
            # MDSplus.mdsExceptions.TreeNOCURRENT: %TREE-E-NOCURRENT, No current shot number set for this tree.
            # 是不是我这数据库的问题，没有完全克隆过来
            print(e)
            shot_num = None
        return shot_num


    def renameChaName(self, channel_name,):
        cha_name = channel_name.upper()
        if cha_name in self.channel_dic['AI']:
            rename = 'AI:' + cha_name
        elif cha_name in self.channel_dic['FBC']:
            rename = 'FBC:' + cha_name
        else:
            rename = None
            print('channel_name is error!')
        return rename


    def isHaveData(self, channel_name):
        # 返回数据长度
        length = self.tree.getNode(self.renameChaName(channel_name)).getLength()
        # length = self.tree.getNode(self.renameChaName(channel_name)).getCompressedLength()
        return length


    def getData(self, channel_name):
        if self.isHaveData(channel_name):
            xAis = self.tree.getNode(self.renameChaName(channel_name)).getData().dim_of()
            value = self.tree.getNode(self.renameChaName(channel_name)).data()
            # data = [xAis, value,]
            # 转化成列表很费时间
            data = [(list(xAis), list(value)]
            return data
        else:
            print('This channel has no data!')
            return []



if __name__ == '__main__':
    tree = mdsTree('exl50_copy', 3602,)
    channel = 'ip'

    print(tree.getData(channel)[0][-1])
    print(tree.getData(channel)[1][-1])

    tree.close()



