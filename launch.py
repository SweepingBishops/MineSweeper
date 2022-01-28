#!/usr/bin/python3.8
import tkinter
from plantMines import plantMines, identifyNeighbouringSquares
from functools import partial
from time import time
from PIL import Image, ImageTk
import youwon


def main(gridSize,mineCount):
	###Global variables###
	result = None
	firstClickFlag,gameover = True, False
	bIdentity , minePositions , squareValues = {}, {}, {}
	startTime, endTime, clickedSquares = 0,0,0

	def leftClick(i,j):
		nonlocal result,gameover, firstClickFlag, clickedSquares ,minePositions, squareValues, startTime, endTime

		button = bIdentity[(i,j)]	#stores the object at (i,j) into local variable button
		if button['image'] or gameover:	#button press function is not executed if the game is over or the button is flagged
			return
		button['state'] = 'disabled'	#so that the same button can't be clicked multiple times

		if firstClickFlag:
			minePositions, squareValues = plantMines(i,j,gridSize,mineCount)	#the mines are planted at the first click
			firstClickFlag = False
			startTime = time()	#stores the time when the user starts playing

		if (i,j) not in minePositions:	#if clicked square does not contain mine it is coloured green
			button.configure(text = squareValues[(i,j)], bg = 'green',activebackground = 'green')
			clickedSquares += 1	
		else:				#if the square contains a mine it is coloured red
			for mine in minePositions:	#all the other mines are coloured orange
					bIdentity[mine].configure(height=46, width=62, bg='orange', activebackground='orange', image=mineImage)
			button.configure(height=46, width=62, bg = 'red', activebackground = 'red', image=mineImage)
			gameover = True
			result = 'You Lost:('
			youwon.disp(result)
			return 'You Lost:('

		if clickedSquares == (gridSize**2 - mineCount):		#checks if the game is won
			endTime = time()	#stores time when the game is won
			gameover = True
			for mine in minePositions:	#All mines are exposed.
				bIdentity[mine].configure(height=46,width=62,image = flagImage)

			score = round(endTime - startTime)
			hours = score//3600
			score %= 3600
			minutes = score//60
			seconds = score%60

			#print(f'Time taken:{hours}h {minutes}min {seconds}s')
			result = f'You Won!\n{hours}:{minutes}:{seconds}'
			youwon.disp(result)
			return f'You Won!\n{hours}:{minutes}:{seconds}'

		if squareValues[(i,j)] == None:		#opens neighbouring squares if current squareValue is 0 (game rule)
			neighbouringSquares = identifyNeighbouringSquares(i, j, gridSize)
			for neighbouringSquare in neighbouringSquares:
				bIdentity[neighbouringSquare].invoke()

	def rightClick(event):
		if gameover: 
			return
		button = event.widget

		if button['image'] == '' and button['bg'] == '#d9d9d9':		#Flags the square if it isn't and is not already leftClicked.
			button.configure(height=46,width=62,image = flagImage)
		elif button['image'] == 'pyimage1':	#Unflags the square.
			button.configure(height = 2, width = 4, image = '')
			
	#creating main window
	global mainWindow
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
	gridSize = None
	while gridSize == None:
		try:
			gridSize = int(input('Enter grid size: '))
			mineCount = int(input('Enter number of mines: '))
			if gridSize < 4:
				raise Exception('Grid size must at least 4.\n')
			elif mineCount > gridSize**2 - 10 or mineCount < 1:
				raise Exception(f'For grid size = {gridSize} the number of mines should be between 1 and {max(gridSize**2 - 10,1)}.\n')
			break                    
		except ValueError:
			gridSize = None
			print('Invalid Input\n')

		except Exception as error:
			print(error.args[0])
			gridSize = None

	main(mainWindow,gridSize,mineCount)