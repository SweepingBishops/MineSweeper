from tkinter import *
import random
import time
from plantMines import *

def openSquares(clickPosition):
	neighbouringSquares =[				#sets the neighbouring squares of the square with index (i,j)
	( i-1 , j-1 ) , ( i , j-1 ) , ( i+1 , j-1 ),
	( i-1 , j )   ,               ( i+1 , j ),
	( i-1 , j+1 ) , ( i , j+1 ) , ( i+1 , j+1 )]



def onClick(clickPosition):
	print(clickPosition)
	if clickPosition not in minePositions:	#if clicked square does not contain mine it is coloured green
		Label(main,text= str(clickPosition[0]) +','+ str(clickPosition[1]),bg='green').grid(row=clickPosition[0],column=clickPosition[1])
		#open_squares
	else:	#if the square contains a mine it is coloured red and the game exits
		Label(main,text= str(clickPosition[0]) +','+ str(clickPosition[1]),bg='red').grid(row=clickPosition[0],column=clickPosition[1])
		print('You lost:(')
		#high scores
		main.after(2000,func=exit)
		


gridSize = int(input('Enter grid size: '))
mineCount = int(input('Enter number of mines: '))
minePositions , squareValues = plantMines(gridSize,mineCount)

#creating main screen
main = Tk(className='Minesweeper')
#main.geometry('250x250')
#adjisting grid size
#main.columnconfigure(0,weight=3)
#main.rowconfigure(0,weight=3)

for i in range(gridSize):
	for j in range(gridSize):
		Button(main,text=str(i)+','+str(j),command=lambda i=i , j=j: onClick((i,j))).grid(row=i,column=j)
		#i is the row number and j is the column number
print(minePositions)
print(squareValues)
mainloop()