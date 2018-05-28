#!/usr/bin/env python
#coding=utf-8

#IO base function
myFile = 0;

def readFile() :
    myFile = open("myText.txt","r+")
   
    print "FileName :",myFile.name;
    print "OpenMode :",myFile.mode
    print "IsClose :", myFile.closed

    str = myFile.read(15);
    print "File read string :" ,str;
    str2= myFile.read(10);
    print "File read String:" ,str2;
    print "当前指针位于:", myFile.tell();
    myFile.seek(0,0);


    str3 = myFile.read(20);
    print "重新读取:",str3

    myFile.close();


def writeFile():
     myFile = open("myText.txt","ab+")
     myFile.write("this my input string");
     myFile.close();

writeFile();
readFile();