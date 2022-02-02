import tkinter as tk
from functools import partial
from highscore import addHighScore
from play import play
def display(result,gridSize):
	global root
	root=tk.Tk()
	root.title('MINESWEEPER')
#frames
	frame1=tk.Frame(master=root,relief=tk.SUNKEN,borderwidth=2)
	frame1.pack(side=tk.LEFT)
	frame1.rowconfigure([0,2,1,3],minsize=50)
	frame1.columnconfigure([0],minsize=150)

	frame2=tk.Frame(master=root)
	frame2.rowconfigure([0,1,2,3],minsize=50)
	frame2.columnconfigure([0],minsize=110)
	frame2.pack()

#buttons
	global button2
	button1=tk.Button(master=frame2,text='Play Again',width=12,height=2,command=play)
	button1.grid(row=2,column=0)
	button2=tk.Button(master=frame2,text='Add Score',width=12,height=2,command=partial(addScore,result,gridSize))
	button2.grid(row=1,column=0)
	button3=tk.Button(master=frame2,text='Quit',width=12,height=2,command=quit)
	button3.grid(row=3,column=0)

#labels
	global label1
	label1=tk.Label(master=frame1,text=result)
	label1.grid(row=1,column=0,sticky='news')
	label2=tk.Label(master=frame1,text='    Enter Name:')
	label2.grid(row=2,column=0,sticky='ws')
#entry
	global entry1
	entry1=tk.Entry(master=frame1)
	entry1.grid(row=3,column=0,sticky='n')
	
	if gridSize==None:
		entry1['state']='disabled'
		label2['state']='disabled'
		button2['state']='disabled'
def addScore(result,gridSize):
	if not entry1.get():
		label1.configure(text='Please enter name')
		return
	#global button1
	name=entry1.get()
	time=result[-8:]
	addHighScore(gridSize,name,time)
	label1.configure(text='Success!')
	button2['state']='disabled'
	
def quit():
	root.destroy()
	exit()
