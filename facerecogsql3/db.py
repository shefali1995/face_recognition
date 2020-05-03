import sqlite3

conn=sqlite3.connect("FaceBase.db")
cur=conn.cursor()
sn=0
while(True):
    id=raw_input("Enter id?")
    Name=raw_input("Enter name?")
    cur.execute("INSERT INTO People(ID,Name) Values("+str(id)+",'"+str(Name)+"')")
    sn=sn+1
    if(sn>1):
      break;

cur.execute("SELECT * FROM People")
data=cur.fetchall()
f=open("C:/Users/harshit/Desktop/facerecogsql/data.txt",'w')
for row in data:
    f.write(str(row[0])+" "+str(row[1])+"\n")
f.close()
conn.commit()
conn.close()



    
    
