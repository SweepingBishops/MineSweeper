import mysql.connector as mc
import tabulate
import tkinter as tk
conn=mc.connect(host='localhost',user='root',database='minesweeper',passwd='rachu@004')
cur=conn.cursor()
cur.execute('select * from gridsize4 order by time;')
b=list(cur)
d=[]
for i in range(5):
    c=list(b[i])
    c.insert(0,i+1)
    d+=[c]

a=tabulate.tabulate(d)

#tkinter
root=tk.Tk()
root.title('HIGHSCORE')
root.rowconfigure([0],minsize=150)
root.columnconfigure([0,1,2],minsize=70)
label=tk.Label(text=a)
label.grid(row=0,column=1)
