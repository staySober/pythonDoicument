#!/usr/bin/env python
#coding=utf-8
import random

def randomPrint() :
    dir = {};
    for i in range(0,100) :
          randomNum = random.randrange(1,101,1);
          print (randomNum)
          if (dir.has_key(randomNum)):
                originalValue = dir[randomNum]
                dir[randomNum] = originalValue + 1
          else:
                dir[randomNum] =1;
    print ("循环10次,1-100随机数中 每一个数出现的次数: ---->")
    for key,value in dir.items() :
        print (key ,"出现" , value , "次");
    return;

def inputPythonExpression():
    str = input("请输入python表达式:");
    print ("你的输入: " , str);

def myList() :
    thisList = [x*5 for x in range (2,10,2)]
    print (thisList);

myList();