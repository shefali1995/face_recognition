import sqlite3

conn=sqlite3.connect("FaceBase.db")
cmd2="SELECT * FROM People"
curso=conn.execute(cmd2)
for row in curso:
    cmd="UPDATE People SET Status='Absent' ,Alerts=NULL , ArrivalTime='' WHERE ID="+str(row[0])
    conn.execute(cmd)
conn.commit()
conn.close()
	