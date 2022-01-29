import tkinter as tk
import os
from functools import partial
import launch
import youwon
def main2():
	global root
	root=tk.Tk()
	root.title('MINESWEEPER')

	root.columnconfigure([0,2],minsize=75)
	root.columnconfigure([1],minsize=150)
	root.rowconfigure([0,1,2,3,4],minsize=50)

	#buttons
	global button1,button2,button3
	button1=tk.Button(text='Play',command=play)
	button1.grid(row=1,column=1,sticky='nsew')
	button2=tk.Button(text='Highscore',command=high)
	button2.grid(row=2,column=1,sticky='nsew')
	button3=tk.Button(text='Quit',command=Quit)
	button3.grid(row=3,column=1,sticky='nesw')


#functions

def play():
	if __name__ == '__main__':
		global button1,button2,button3
		button1.destroy()
		button2.destroy()
		button3.destroy()
	else:
		global root
		root = tk.Tk()
		youwon.root.destroy()
		launch.mainWindow.destroy()

	button1=tk.Button(root,text='gridsize=4*4',command=partial(game,4))
	button1.grid(row=1,column=1,sticky='nsew')
	button2=tk.Button(root,text='gridsize=8*8',command=partial(game,8))
	button2.grid(row=2,column=1,sticky='nsew')
	button3=tk.Button(root,text='gridsize=10*10',command=partial(game,10))
	button3.grid(row=3,column=1,sticky='nesw')

def game(gridsize):
	root.destroy()
	launch.main(gridsize,6)

def Quit():
	root.destroy()

def high():
	root.destroy()
	import highscore 

if __name__=='__main__':
	main2()
	root.mainloop()
