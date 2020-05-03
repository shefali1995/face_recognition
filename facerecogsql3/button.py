import sys
import os
from Tkinter import *
from tkMessageBox import *


top=Tk()
row=Frame(top)
T1=Text(row,height=20,width=50)
photo=PhotoImage(file='C:/Users/harshit/Desktop/facerecogsql/attendanceonline1.gif')
T1.insert(END, '\n')
T1.image_create(END,image=photo)
row.pack(side="top",fill=X)
T1.pack(side="left")

T2=Text(row,height=20,width=50)
T2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
T2.tag_configure('big', font=('Verdana', 20, 'bold'))
T2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))
T2.tag_bind('follow', '<1>', lambda e, t=T2: t.insert(END, "Not now, maybe later!"))
T2.insert(END, "\n    FACE RECOGNITION  \n   ATTENDANCE MARKING \n              SYSTEM\n",'big')
T2.pack(side="left")


def helloCallBack():
    os.system('datasetcr.py')

B=Button(top,text="New User",fg="red",command= helloCallBack)


def helloCallBack1():
    os.system('detector.py')

B1=Button(top,text="Registered User",fg="red",command= helloCallBack1)

def helloCallBack2():
    os.system('mailer.py')

B2=Button(top,text="Send Mail",fg="red",command= helloCallBack2)
def callback():
    if askyesno('Verify', 'Really quit?'):
        B3.quit()
    else:
        showinfo('No', 'Quit has been cancelled')


B3=Button(top,text="EXIT",fg="red",command= callback)
def callback1():
    os.system('reset.py') 
B4=Button(top,text="RESET",fg="red",command= callback1)
def callback2():
    os.system('view.py')
B5=Button(top,text="VIEW",fg="red",command= callback2)

B.pack(side="left",padx="40")
B1.pack(side="left",padx="40")
B2.pack(side="left",padx="40")
B3.pack(side="left",padx="40")
B4.pack(side="left",padx="40")
B5.pack(side="left",padx="40")
top.mainloop()

top.destroy()

 
