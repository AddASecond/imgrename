# coding: UTF-8

import os
def directory(rootdir):                                  #指明被遍历的文件夹
    for parent,dirnames,filenames in os.walk(rootdir):   #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字            
        for dirname in  dirnames:                        #输出文件夹信息
            print "parent is:" + parent
            print "dirname is:" + dirname

        for filename in filenames:
            print "parent is:" + parent                  #输出文件夹信息
            print "filename is:" + filename              #输出文件信息
            filenameNew = filename[:-7] + "4_0.jpg"
            print "new filename is:" + filenameNew
            oldDir = os.path.join(parent,filename)
            #print "the full oldDir of the file is:" + oldDir  #输出文件路径信息
            newDir = os.path.join(parent,filenameNew)
            #print "the full newDir of the file is:" + newDir  #输出文件路径信息
            os.rename(oldDir,newDir);  #重命名


directory('D:\\06TestImg\\02ForTestOnly\\测试')
