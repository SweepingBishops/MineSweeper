import tabulate
import tkinter as tk
import menu1

import mysql.connector as mc
conn=mc.connect(host='localhost',user='root',database='minesweeper',passwd='rachu@004')
cur=conn.cursor()

#tkinter
root=tk.Tk()
root.title('HIGHSCORE')

#frames
frame1=tk.Frame()
frame1.pack()
frame1.rowconfigure([0,2],minsize=40)
frame1.rowconfigure([1],minsize=150)
frame1.columnconfigure([0,1,2],minsize=160)

frame2=tk.Frame()
frame2.pack()

#definition
def back():
    root.destroy()
    menu1.main2()


#gridsize6
cur.execute('select * from gridsize6 order by time;')
b=list(cur)
d=[]
for i in range(5):
    c=list(b[i])
    c.insert(0,i+1)
    d+=[c]
head=['Rank','Name','Time']    
a=tabulate.tabulate(d,headers=head)
label=tk.Label(master=frame1,text=a)
label.grid(row=1,column=0)

#gridsize8
cur.execute('select * from gridsize8 order by time;')
b=list(cur)
d=[]
for i in range(5):
    c=list(b[i])
    c.insert(0,i+1)
    d+=[c]
head=['Rank','Name','Time']    
a=tabulate.tabulate(d,headers=head)
label=tk.Label(master=frame1,text=a)
label.grid(row=1,column=1)
#gridsize10
cur.execute('select * from gridsize10 order by time;')
b=list(cur)
d=[]
for i in range(5):
    c=list(b[i])
    c.insert(0,i+1)
    d+=[c]
head=['Rank','  Name  ','Time']    
a=tabulate.tabulate(d,headers=head)
label=tk.Label(master=frame1,text=a)
label.grid(row=1,column=2)

#buttons
button=tk.Button(master=frame2,text='Back',height=2,width=10,command=back)
button.pack()



