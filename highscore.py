from tabulate import tabulate
import tkinter as tk
import mysql.connector as mysql
def display():
	db=mysql.connect(host='localhost',user='root',database='minesweeper',passwd='')
	cursor=db.cursor()

#tkinter
	root=tk.Tk()
	root.title('HIGHSCORE')

#frames
	frame1=tk.Frame(root)
	frame1.pack()
	frame1.rowconfigure([0,2],minsize=40)
	frame1.rowconfigure([1],minsize=150)
	frame1.columnconfigure([0,1,2],minsize=160)

	frame2=tk.Frame(root)
	frame2.pack()

#gridsize6
	cursor.execute('select * from gridsize6 order by time;')
	data=list(cursor)
	displayedData=[]
	try:
		for rank in range(5):
			displayedData += [[rank+1]+list(data[rank])]

	except IndexError:
	    pass
	header=['Rank','Name','Time']    
	label=tk.Label(master=frame1,text='Grid Size 6x6 5 mines\n'+tabulate(displayedData,headers=header,tablefmt='psql'),font=('Consolas',11))
	label.grid(row=1,column=0)

#gridsize8
	cursor.execute('select * from gridsize8 order by time;')
	data=list(cursor)
	displayedData=[]
	try:
		for rank in range(5):
			displayedData += [[rank+1]+list(data[rank])]

	except IndexError:
	    pass
	header=['Rank','Name','Time']    
	label=tk.Label(master=frame1,text='Grid Size 8x8 10 mines\n'+tabulate(displayedData,headers=header,tablefmt='psql'),font=('Consolas',11))
	label.grid(row=1,column=1)
#gridsize10
	cursor.execute('select * from gridsize10 order by time;')
	data=list(cursor)
	displayedData=[]
	try:
		for rank in range(5):
			displayedData += [[rank+1]+list(data[rank])]

	except IndexError:
	    pass
	header=['Rank','Name','Time']    
	label=tk.Label(master=frame1,text='Grid Size 10x10 15 mines\n'+tabulate(displayedData,headers=header,tablefmt='psql'),font=('Consolas',11))
	label.grid(row=1,column=2)


def  addHighScore(gridSize,username,time):   
    db=mysql.connect(host='localhost',user="root",password="",charset = "utf8",database="minesweeper")
    cursor=db.cursor()
    cursor.execute(f"insert into gridsize{gridSize} values('{username}','{time}')")
    db.commit()

