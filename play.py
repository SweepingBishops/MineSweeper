import tkinter as tk
from _tkinter import TclError
from functools import partial
import gameWindow
import endScreen
import highscore 
def main():
	global root
	root=tk.Tk()
	root.title('MINESWEEPER')

	root.columnconfigure([0,2],minsize=75)
	root.columnconfigure([1],minsize=150)
	root.rowconfigure([0,1,2,3,4],minsize=50)

	#buttons
	global button1,button2,button3
	button1=tk.Button(text='Play',command=play)
	button2=tk.Button(text='Highscore',command=high)
	button3=tk.Button(text='Quit',command=Quit)

	button1.grid(row=1,column=1,sticky='nsew')
	button2.grid(row=2,column=1,sticky='nsew')
	button3.grid(row=3,column=1,sticky='nesw')


#functions

def play():
	if __name__ == '__main__':
		global button1,button2,button3
		button1.destroy()
		button2.destroy()
		button3.destroy()
	else:
		try:
			endScreen.root.destroy()
			gameWindow.mainWindow.destroy()
		except TclError:
			pass

		global root
		root = tk.Tk()
		root.columnconfigure([0,2],minsize=75)
		root.columnconfigure([1],minsize=150)
		root.rowconfigure([0,1,2,3,4],minsize=50)

	button1=tk.Button(root,text='gridsize=6x6\n5 mines',command=partial(game,6,5))
	button2=tk.Button(root,text='gridsize=8x8\n10 mines',command=partial(game,8,10))
	button3=tk.Button(root,text='gridsize=10x10\n15 mines',command=partial(game,10,15))

	button1.grid(row=1,column=1,sticky='nsew')
	button2.grid(row=2,column=1,sticky='nsew')
	button3.grid(row=3,column=1,sticky='nesw')

def game(gridSize,mineCount):
	root.destroy()
	gameWindow.main(gridSize,mineCount)

def Quit():
	root.destroy()

def high():
	highscore.display()

if __name__=='__main__':
	main()
	root.mainloop()
