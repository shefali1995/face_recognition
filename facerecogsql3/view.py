import os
from Tkinter import *
from tkFileDialog import askopenfilename
import datetime
from tkMessageBox import *

def passw():
  while True:
  
    master = Tk()
    Label(master, text="Password:").grid(row=0)
    e1 = Entry(master,show='*')
    e1.grid(row=0, column=1)
    e1.focus()
    Button(master, text='SUBMIT', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    master.mainloop( )
    #master.destroy()
    password=e1.get()
    if(password=='sweety'):
       showfile()	  
    else:
	showinfo('error','Incorrect password')

def showfile():
    master1 = Tk()
    Label(master1, text="Date(dd-m-yy):").grid(row=0)
    e2 = Entry(master1)
    e2.grid(row=0, column=1)
    e2.focus()
    Button(master1, text='SUBMIT', command=master1.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    master1.mainloop( )
    date=e2.get()
#    logged()	
#def logged():
    path= "C:/Users/harshit/Desktop/facerecogsql3/attendance/"
      #now = datetime.datetime.now()
      #lst=list()
      #lst.insert(0,now.day)
      #lst.insert(1,now.month)
      #lst.insert(2,now.year)
      #date=str(lst[0])+"-"+str(lst[1])+"-"+str(lst[2])
    newname = date+'.xls'
    os.startfile(path+newname)
    sys.exit()
passw()
