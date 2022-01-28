import tkinter as tk
import menu1
def disp(a):
	#print(a)
	global root
	root=tk.Tk()
#frames
	frame1=tk.Frame(master=root,relief=tk.SUNKEN,borderwidth=2)
	frame1.pack(side=tk.LEFT)
	frame1.rowconfigure([0,2,1,3],minsize=50)
	frame1.columnconfigure([0],minsize=150)

	frame2=tk.Frame(master=root)
	frame2.rowconfigure([0,1,2,3],minsize=50)
	frame2.columnconfigure([0],minsize=110)
	frame2.pack()

#functions
##def add_highscore():

#buttons
	button1=tk.Button(master=frame2,text='Try Again',width=12,height=2,command=menu1.play)
	button1.grid(row=2,column=0)
	button2=tk.Button(master=frame2,text='Add highscore',width=12,height=2)
	button2.grid(row=1,column=0)

#labels
	label1=tk.Label(master=frame1,text=a)
	label1.grid(row=1,column=0,sticky='news')
	label2=tk.Label(master=frame1,text='    enter name:')
	label2.grid(row=2,column=0,sticky='ws')
#entry
	entry1=tk.Entry(master=frame1)
	entry1.grid(row=3,column=0,sticky='n')
