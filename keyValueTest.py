#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math
import random

#字典
KeyValue = {
    "age": 123,
    "country":"china",
    "name":"kevin"
}

for i in KeyValue : print(i), ;print(KeyValue[i]),

# Pass块
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"

doubleNum = -2.54;
print(math.ceil(doubleNum));
print(math.floor(doubleNum));
print(round(doubleNum, 1));
print(abs(doubleNum));

for i in range(1,10) :
            print(random.choice(range(10)));

# random
print "random() : ",  random.random();

#字符串操作
str1="Hello Kevin"
print "str1 substring:" , str1[:6];
print "replace str1:", str1[:5] + " Sober";

#转义字符
print "\\"
print"\a"
print"\r"
print"\t"

#字符串运算符
a = "Hello"
print a * 5
print("H" in a)
print("H" not in a)
print '\n'

#格式化字符串
print "My name is %s,age is %d"%("kevin",21);

#复杂字符串
complicatedStr = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print complicatedStr;

#字符串内建函数
print(complicatedStr.center(100))

#ListJ截取
list1 = ["123","4556","daffe","231d"];
listSubStr = list1[0:2]
print(listSubStr)
print list1

list1[1] = "修改了"
list1.append("append");
print list1;
print list1[1]

list3 = list1 + listSubStr;
print list3;

list4 = list3 * 2;
print list4;

print "123" in list4;

#元组   元组和列表类似 但是不允许修改元组元素
yuanZU = (123,45,54)

yuanZU2 = yuanZU *2
print yuanZU2;

del yuanZU2;
#抛出异常
#print yuanZU2;