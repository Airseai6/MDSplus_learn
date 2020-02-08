# -*- coding:utf-8 -*-
# @CreateTime : 2020/2/8 17:29
# @Author     : Qi

from MDSplus import Tree

def getParam(dbname,shot):
    t=Tree(dbname,shot)
    # t.setTimeContext(0,11,0.03)
    data=t.getNode("fbc:ip").data()
    data_list = [item for item in data]
    data_list = data_list[:-2]
    return data_list


if __name__ == '__main__':
    data = getParam('exl50_copy', 3602)
    print(type(data))
    print(len(data))
    # print(data[0])
    # print(data)