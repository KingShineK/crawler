# _*_ coding:utf-8 _*_
import csv

c=open(r"e:/test.csv","r+")
#read=csv.reader(c)
#for line in read:
#    print line
read=c.readlines()
print read
c.close()