#!/usr/bin/python3.8
import tkinter
from plantMines import plantMines, identifyNeighbouringSquares
from functools import partial
from time import time
from PIL import Image, ImageTk

###Global variables###
firstClickFlag = True
bIdentity , minePositions , squareValues = {}, {}, {}
clickedSquares = 0
startTime, endTime = 0,0

def main():
	def leftClick(i,j):
		global firstClickFlag, minePositions, squareValues, clickedSquares, startTime, endTime

		button = bIdentity[(i,j)]	#stores the object at (i,j) into local variable button
		if button['image'] != '':	#if the square is flagged then it cannot be clicked
			return
		button['state'] = 'disabled'	#so that the same button can't be clicked multiple times

		if firstClickFlag:
			minePositions, squareValues = plantMines(i,j,gridSize,mineCount)	#the mines are planted at the first click
			firstClickFlag = False
			startTime = time()

		if (i,j) not in minePositions:	#if clicked square does not contain mine it is coloured green
			button.configure(text = squareValues[(i,j)], bg = 'green',activebackground = 'green')
		else:				#if the square contains a mine it is coloured red
			button.configure(height=46, width=62, bg = 'red', activebackground = 'red', image=mineImage)
			for button in bIdentity.values():     #All buttons are diabled once a mine is clicked and the rest of the mines are shown 
				button['state'] = 'disabled'
				for mine in minePositions:
					if mine != (i,j):
						bIdentity[mine].configure(height=46, width=62, bg='orange', activebackground='orange', image=mineImage)
			print('You lost:(')

		clickedSquares += 1	

		if squareValues[(i,j)] == None:		#opens neighbouring squares if current squareValue is 0 (game rule)
			neighbouringSquares = identifyNeighbouringSquares(i, j, gridSize)
			for neighbouringSquare in neighbouringSquares:
				bIdentity[neighbouringSquare].invoke()

		if clickedSquares == (gridSize**2 - mineCount):
			print('You won!')
			endTime = time()
			for button in bIdentity.values():	#All buttons are disabled once the game is won.
				button['state'] = 'disabled'
				for mine in minePositions:	#All mines are exposed.
					bIdentity[mine].configure(bg='blue',activebackground='blue')
			print(f'Time taken:{round(endTime - startTime,2)}s')


	def rightClick(event):
		button = event.widget

		if button['image'] == '' and button['bg'] == '#d9d9d9':		#Flags the square if it isn't and is not already leftClicked.
			button.configure(height=46,width=62,image = flagImage)
		elif button['image'] == 'pyimage1':	#Unflags the square.
			button.configure(height = 2, width = 4, image = '')
			
	gridSize = None
	while gridSize == None:
			try:
				gridSize = int(input('Enter grid size: '))
				mineCount = int(input('Enter number of mines: '))
				if mineCount > gridSize**2 - 10:
					raise Exception
				break
			except ValueError:
				gridSize = None
				print('Invalid Input\n')

			except Exception:
				print(f'For grid size = {gridSize} the number of mines should be between 1 and {gridSize**2 - 10}.\n')
				gridSize = None
	#creating main window
	mainWindow = tkinter.Tk(className='Minesweeper')
	mainWindow.option_add('*Font','22')
	#images for the mine and the flag
	flagImage = ImageTk.PhotoImage(Image.open('resources/flag.png').resize((50,50)))
	mineImage = ImageTk.PhotoImage(Image.open('resources/mine.png').resize((50,50)))

	for i in range(gridSize):
		for j in range(gridSize):
			#creates and sets the buttons onto the window
			button = tkinter.Button(mainWindow,disabledforeground = 'black', command = partial(leftClick,i,j), height = 2, width = 4)
			button.grid(row=i,column=j)
			button.bind("<Button-3>",rightClick)
			
			bIdentity[(i,j)] = button	#adds the object into the dictionary so that it can be used later
			
	mainWindow.mainloop()

if __name__ == '__main__':
	main()
