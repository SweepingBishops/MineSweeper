from tkinter import *
import random
import time
from plantMines import *

###Global variables###
firstClickFlag = True
minePositions , squareValues = {}, {}

def onClick(i,j):
	global firstClickFlag
	global minePositions
	global squareValues

	if firstClickFlag:
		minePositions, squareValues = plantMines(i,j,gridSize,mineCount)
		print(minePositions)
		firstClickFlag = False

	if (i,j) not in minePositions:	#if clicked square does not contain mine it is coloured green
		Label(main,text= squareValues[(i,j)],bg='green').grid(row=i,column=j)
		#open_squares
	else:	#if the square contains a mine it is coloured red and the game exits
		Label(main,text= str(i) +','+ str(j),bg='red').grid(row=i,column=j)
		print('You lost:(')
		#high scores
		main.after(2000,func=exit)
		


gridSize = int(input('Enter grid size: '))
mineCount = int(input('Enter number of mines: '))

#creating main screen
main = Tk(className='Minesweeper')
#adjisting grid size
#main.columnconfigure(0,weight=3)
#main.rowconfigure(0,weight=3)

for i in range(gridSize):
	for j in range(gridSize):
		Button(main,text=str(i)+','+str(j),command=lambda i=i , j=j: onClick(i,j)).grid(row=i,column=j)
		#i is the row number and j is the column number
#print(squareValues)
mainloop()
