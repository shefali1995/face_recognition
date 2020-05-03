import cv2,os,sys
import numpy as np
from PIL import Image
import sqlite3
import pickle
from Tkinter import *
from tkMessageBox import *
import datetime
import time
now = datetime.datetime.now()
lrt=list()
lrt.insert(0,now.day)
lrt.insert(1,now.month)
lrt.insert(2,now.year)
date=str(lrt[0])+"-"+str(lrt[1])+"-"+str(lrt[2])
r=0
s=0
newpath1="C:/Users/harshit/Desktop/facerecogsql3/FRAUD ENTRY/"
dirList1 = os.listdir(newpath1)
for fname1 in dirList1:
    if(fname1=='xyz' and r==0):
       r=1
    elif(fname1!=date and r==1):
        os.makedirs(newpath1+date)
newpath2="C:/Users/harshit/Desktop/facerecogsql3/ILLEGAL ATTEMPT/"
dirList2=os.listdir(newpath2)
for fname2 in dirList2:
    if(fname2=='xyz' and s==0):
       #os.remove(newpath2+'xyz')
       s=1
    elif(fname2!=date and s==1):
        os.makedirs(newpath2+date)
master = Tk()
Label(master, text="Enter Password").grid(row=0)
e1 = Entry(master,show='*')
e1.grid(row=0, column=1)
e1.focus()
Button(master, text='SUBMIT', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
master.mainloop( )
password=e1.get()
ratio=0	    
mini=0
maxi=0
recognizer=cv2.createLBPHFaceRecognizer(1,8,7,7,100.0)
recognizer.load("recognizer/trainingData"+str(password)+".yml")
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml");
path='dataSet/'+str(password)
stat='Absent'
c=1
lst=[]
profile=None
Img=None
def getProfile(Password,confi):
    lst.append(confi)
    stat='Absent'
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE Password="+str(Password)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
         profile=row
    conn.commit()
    conn.close()
    return profile

	  
	
cam=cv2.VideoCapture(0);
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,1,2)
def consta() :
    cam.release()
t=time.time()+10
while(True):
    ret,img=cam.read();
    Img=img
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=6,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE);
    for(x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(password,conf)

        if(profile !=None and conf<35):
            cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[0]),(x,y+h+30),font,225);
            cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+70),font,225);
            cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),(x,y+h+100),font,225);
            cv2.cv.PutText(cv2.cv.fromarray(img),str(conf),(x+150,y+h+150),font,225);
		
	 
    cv2.imshow("Face",img);
    cv2.waitKey(10)
    
    if(time.time()>t):
	     break
for i in lst:
    if(i<30):
        mini=mini+1
    if(i>50):
        maxi=maxi+1

ratio=mini/maxi
print ratio


if(ratio>1.5):
   stat="Present"
   time=str(datetime.datetime.now().strftime('%H:%M:%S'))
   conn=sqlite3.connect("FaceBase.db") 
   cmd1="UPDATE People SET Status='"+stat+"',ArrivalTime='"+time+"' WHERE Password="+str(password)
   conn.execute(cmd1)
   conn.commit()  
   conn.close()
else:
    if(profile[3]=='Absent'):
        aler="ILLEGAL ATTEMPT"
        cv2.imwrite("C:/Users/harshit/Desktop/facerecogsql3/ILLEGAL ATTEMPT/"+date+"/"+str(profile[0])+".jpg",Img[y:y+h,x:x+w])	
    if(profile[3]=='Present'):
	aler="Fraud"
	cv2.imwrite("C:/Users/harshit/Desktop/facerecogsql3/FRAUD ENTRY/"+date+"/"+str(profile[0])+".jpg",Img[y:y+h,x:x+w])
    time=str(datetime.datetime.now().strftime('%H:%M:%S'))
    conn=sqlite3.connect("FaceBase.db") 
    cmd2="UPDATE People SET Alerts='"+aler+"',ArrivalTime='"+time+"' WHERE Password="+str(password)
    conn.execute(cmd2)
    conn.commit()

os.system('data.py')

    

    
