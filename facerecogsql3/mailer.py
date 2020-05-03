import os
import smtplib
import getpass
import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from Tkinter import Tk
from tkFileDialog import askopenfilename
from Tkinter import *
from tkMessageBox import *
q=0
now = datetime.datetime.now()
lst=list()
lst.insert(0,now.day)
lst.insert(1,now.month)
lst.insert(2,now.year)
date=str(lst[0])+"-"+str(lst[1])+"-"+str(lst[2])+".xls"
def send(name, passwd, subject, body, addrto, q):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] =name+ '@gmail.com' 
    msg['To'] = addrto

    text = MIMEText(body)
    msg.attach(text)

    if(q == 1):
        part = MIMEBase('application', "octet-stream")
        path = str(askopenfilename())
        f = open(path,'rb')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=str(date))           
        msg.attach(part)

        #img_data = open(img, 'rb').read()
        #image = MIMEText(img_data,os.path.basename(img))
        #msg.attach(image)

    showinfo('Message','Connecting')
    s = smtplib.SMTP('smtp.gmail.com', '587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(name, passwd)
    showinfo('Message','Connected')
    s.sendmail(name + '@gmail.com', addrto, msg.as_string())
    showinfo('Message','Sent')
    s.quit()

Tk().withdraw()


def show_entry_fields():
   print("UserName: %s" % (e1.get()))
   print("Password: %s" % (e2.get()))
   print("Subject: %s" % (e3.get()))
   print("Body: %s" % (e4.get()))
   print("AddressTo: %s" % (e5.get()))
master = Tk()
Label(master, text="UserName").grid(row=0)
Label(master, text="Password").grid(row=1)
Label(master, text="Subject").grid(row=2)
Label(master, text="Body").grid(row=3)
Label(master, text="AddressTo").grid(row=4)
e1 = Entry(master)
e2 = Entry(master,show='*')
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e1.focus()
Button(master, text='SUBMIT', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='SHOW', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
master.mainloop( )
name=e1.get()
if(name==''):
  showinfo('Error','Cannot be null')
  sys.exit()
passwd=e2.get()
if(passwd==''):
  showinfo('Error','Cannot be null')
  sys.exit()
subject=e3.get()
if(subject==''):
  showinfo('Error','Cannot be null')
  sys.exit()
body=e4.get()
if(body==''):
  showinfo('Error','Cannot be null')
  sys.exit()
addrto=e5.get()
if(addrto==''):
  showinfo('Error','Cannot be null')
  sys.exit()
if askyesno('Message','If you want to attach an excel file'):
  q=1
else:
  showinfo('do not want to attach file')


send(name, passwd, subject, body, addrto, q)