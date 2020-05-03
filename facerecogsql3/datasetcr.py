import cv2,sys
import os
import numpy as np
import sqlite3
from Tkinter import *
from tkMessageBox import *
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml");
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name,College,Password,up):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExists=0
    for row in cursor:
	    if(str(row[0])==Id):
		  isRecordExists=1
    if(isRecordExists==1 and up==1):
	   cmd="UPDATE People SET Name=' "+str(Name)+"' , College=' "+str(College)+"', Status=Absent "+" , ArrivalTime=null ' WHERE ID="+str(Id)
	   
    else:
       cmd="INSERT INTO People(ID,Name,College,Password) Values("+str(Id)+",' "+str(Name)+"','"+str(College)+" ','"+str(Password)+"' )"      
    conn.execute(cmd)
    conn.commit()
    conn.close()
UP=0
#id=raw_input('enter user id>')


def show_entry_fields():
   print("ID: %s" % (e1.get()))
   
master = Tk()
Label(master, text="ID").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
e1.focus()
Button(master, text='SUBMIT', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
master.mainloop( )
id=e1.get()
if(id==''):
  showinfo('Error','Cannot be null')
  sys.exit()

conn1=sqlite3.connect("FaceBase.db")
cmd2="SELECT * FROM People WHERE ID="+str(id)
cursor2= conn1.execute(cmd2)

for row in cursor2:
    if(str(row[0])==id):
	  showinfo('Error','record already exists'+id)
	  if askyesno('Update', 'Do you want to update?'):
	    UP=1
	  else:
	    sys.exit()
conn1.close() 
def show_entry_fields1():
   print("NAME: %s\nCOLLEGE= %s" % (e2.get(),e3.get()))
   
master1 = Tk()
Label(master1, text="NAME").grid(row=0)
Label(master1, text="COLLEGE").grid(row=1)
Label(master1, text="PASSWORD").grid(row=2)
e2 = Entry(master1)
e3 = Entry(master1)
e4 = Entry(master1,show='*')
e2.grid(row=0, column=1)
e3.grid(row=1, column=1)
e4.grid(row=2, column=1)
e2.focus()
Button(master1, text='SUBMIT', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master1, text='SHOW', command=show_entry_fields1).grid(row=3, column=1, sticky=W, pady=4)
master1.mainloop( )
name=e2.get()
college=e3.get()
password=e4.get()
newpath="C:/Users/harshit/Desktop/facerecogsql3/dataSet/"+str(password)
os.makedirs(newpath)
if(name==''):
  showinfo('Error','Name cannot be null')
  sys.exit()
#name=raw_input('enter your name>')
#college=raw_input('enter your college name>')
insertOrUpdate(id,name,college,password,UP)
#conn=sqlite3.connect("FaceBase.db")
#cur=conn.cursor()	
#cur.execute("SELECT * FROM People")
#data=cur.fetchall()
#f=open("C:/Users/harshit/Desktop/facerecogsql/data.txt",'w')
#for row in data:
#    f.write(str(row[0])+" "+str(row[1])+"\n")
#f.close()
#conn.commit()
#conn.close()
sampleNum=0;
k=0
i=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=6,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE);
    for(x,y,w,h)in faces:
        cv2.imwrite(newpath+"/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100)
        sampleNum=sampleNum+1;
        k=k+1
    cv2.imshow("Face",img);
    cv2.waitKey(1);
	
    if(k==10):
		showinfo('error','Change the background')
		i=i+1
		k=0	
    if(i==4):
        break;
cam.release()
cv2.destroyAllWindows()
import trainer
sys.exit()

    
