import tkinter
import random
import time
from plantMines import plantMines, identifyNeighbouringSquares
from functools import partial

###Global variables###
firstClickFlag = True
bIdentity , minePositions , squareValues = {}, {}, {}

def main():

	def onClick(i,j):
		global firstClickFlag
		global minePositions
		global squareValues

		button = bIdentity[(i,j)]
		button['state'] = 'disabled'

		if firstClickFlag:
			minePositions, squareValues = plantMines(i,j,gridSize,mineCount)
			print(minePositions)
			firstClickFlag = False

		if (i,j) not in minePositions:	#if clicked square does not contain mine it is coloured green
			tkinter.Label(mainWindow,text= squareValues[(i,j)],bg='green', height = 1, width = 4).grid(row=i,column=j)

		else:				#if the square contains a mine it is coloured red and the game exits
			tkinter.Label(mainWindow,text= str(i) +','+ str(j),bg='red', height = 1, width = 4).grid(row=i,column=j)
			print('You lost:(')
			mainWindow.after(10000,func=exit)
		if squareValues[(i,j)] == None:
			neighbouringSquares = identifyNeighbouringSquares(i, j, gridSize)
			for neighbouringSquare in neighbouringSquares:
				bIdentity[neighbouringSquare].invoke()


	gridSize = int(input('Enter grid size: '))
	mineCount = int(input('Enter number of mines: '))

	#creating main screen
	mainWindow = tkinter.Tk(className='Minesweeper')
	
	for i in range(gridSize):
		for j in range(gridSize):
			button = tkinter.Button(mainWindow, text= f'{str(i)},{str(j)}', command = partial(onClick,i,j) , height = 1, width = 2)
			#button = tkinter.Button(mainWindow, text=count , command = partial(onClick,i,j) , height = 1, width = 2)
			button.grid(row=i,column=j)
			bIdentity[(i,j)] = button
			#i is the row number and j is the column number
	mainWindow.mainloop()

if __name__ == '__main__':
	main()
