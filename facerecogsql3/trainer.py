import os
import cv2
from Tkinter import *
from tkMessageBox import *
import numpy as np 
from PIL import Image 

master = Tk()
Label(master, text="Confirm Password").grid(row=0)
e1 = Entry(master,show='*')
e1.grid(row=0, column=1)
e1.focus()
Button(master, text='SUBMIT', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
#Button(master, text='SHOW', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
master.mainloop( )
password=e1.get()
recognizer=cv2.createLBPHFaceRecognizer(1,8,7,7,100.0);
path="C:/Users/harshit/Desktop/facerecogsql3/dataSet/"+str(password)

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
         faceImg=Image.open(imagePath).convert('L');
         faceNp=np.array(faceImg,'uint8')
         ID=int(os.path.split(imagePath)[-1].split('.')[1])
         faces.append(faceNp)
         IDs.append(ID)
         cv2.imshow("training",faceNp)
         cv2.waitKey(50)
    return IDs,faces
         
Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainingdata'+str(password)+'.yml')
cv2.destroyAllWindows()
         
