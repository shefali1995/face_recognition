import xlwt
import sqlite3
import datetime
import os,sys
import shutil
now = datetime.datetime.now()
lst=list()
lst.insert(0,now.day)
lst.insert(1,now.month)
lst.insert(2,now.year)
date=str(lst[0])+"-"+str(lst[1])+"-"+str(lst[2])
#print date
path='C:/Users/harshit/Desktop/facerecogsql3/attendance'
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("sheet1")

sheet1.write(0, 0, "ID")
sheet1.write(0, 1, "NAME")
sheet1.write(0, 2, "COLLEGE")
sheet1.write(0, 3, "STATUS")
sheet1.write(0, 4, "ARRIVAL TIME")
sheet1.write(0, 5, "ALERTS")

conn=sqlite3.connect("FaceBase.db")
cmd="SELECT * FROM People"
cursor=conn.execute(cmd)
i=1
for row in cursor:
     sheet1.write(i,0,str(row[0]))
     sheet1.write(i,1,str(row[1]))
     sheet1.write(i,2,str(row[2]))
     sheet1.write(i,3,str(row[3]))
     sheet1.write(i,4,str(row[4]))
     sheet1.write(i,5,str(row[5]))
     i=i+1
newname = date+'.xls'
book.save(newname)
conn.close()

dirList = os.listdir(path) 

for fname in dirList:
    if(fname==newname):
	   os.remove(path+'/'+newname)

shutil.move(newname,path)
