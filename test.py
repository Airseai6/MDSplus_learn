#! python3
# -*- coding:utf-8 -*-
import datetime
import time
def jishi(fun):
   def warper(*args, **kwargs):
      start_time = datetime.datetime.now()
      fun()
      end_time = datetime.datetime.now()
      haoshi = (end_time-start_time).total_seconds()
      print("函数运行耗时{}".format(haoshi))
   return warper()

@jishi
def yunsuan():
   time.sleep(2)
   for x in range(100):
      print(x)
yunsuan()


