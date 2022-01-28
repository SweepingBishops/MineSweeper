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
	tileIdentity , minePositions , squareValues = {}, {}, {}
	startTime, endTime, clickedSquares = 0,0,0
	class tile():
		def __init__(self,mainWindow,xPos,yPos):
			self.xPos=xPos
			self.yPos=yPos
			self.leftClicked,self.rightClicked = False,False
			self.button=tkinter.Button(mainWindow,disabledforeground='black',height=2,width=4)
			self.button.grid(row=xPos,column=yPos)
			self.button.bind("<Button-1>",self.leftClick)
			self.button.bind("<Button-3>",self.rightClick)

		
		def leftClick(self,event=None):
			nonlocal result,gameover,firstClickFlag,clickedSquares,minePositions,squareValues,startTime,endTime
			if self.rightClicked or self.leftClicked or gameover:
				return
			self.leftClicked = True
			if firstClickFlag:
				firstClickFlag = False
				minePositions,squareValues = plantMines(self.xPos,self.yPos,gridSize,mineCount)
				startTime = time()

			if (self.xPos,self.yPos) not in minePositions:
				self.button.configure(text=squareValues[(self.xPos,self.yPos)], bg='green', activebackground='green')
				clickedSquares += 1
			else:
				for mine in minePositions:
					tileIdentity[mine].button.configure(height=46,width=62, bg='orange', activebackground='orange', image=mineImage)
				self.button.configure(height=46, width=62, bg='red', activebackground='red', image=mineImage)
				gameover = True
				if __name__ != '__main__':
					youwon.disp(r'You Lost:(')
				return
			if clickedSquares == (gridSize**2 - mineCount):
				endTime = time()
				gameover = True
				for mine in minePositions:
					pass####
				score = round(endTime - startTime)
				hours = score//3600
				score %= 3600
				minutes = score//60
				seconds = score%60
				result = f'You Won!\n{hours}:{minutes}:{seconds}'
				if __name__ != '__main__':
					youwon.disp(result)
				return

			if squareValues[(self.xPos,self.yPos)] == None:
				neighbouringSquares = identifyNeighbouringSquares(self.xPos,self.yPos,gridSize)
				for neighbouringSquare in neighbouringSquares:
					tileIdentity[neighbouringSquare].leftClick()


		def rightClick(self,event=None):
			if not self.rightClicked and not self.leftClicked:
				self.rightClicked = True
				self.button.configure(height=46, width=62, image=flagImage)
			else:
				self.rightClicked = False
				self.button.configure(height=2, width=4,image='')
	#creating main window
	global mainWindow
	mainWindow = tkinter.Tk(className='Minesweeper')
	mainWindow.option_add('*Font','Ariel 12')
	#images for the mine and the flag
	flagImage = ImageTk.PhotoImage(Image.open('resources/flag.png').resize((50,50)))
	mineImage = ImageTk.PhotoImage(Image.open('resources/mine.png').resize((50,50)))

	for i in range(gridSize):
		for j in range(gridSize):
			#creates and sets the buttons onto the window
			button = tile(mainWindow,i,j)
			tileIdentity[(i,j)] = button	#adds the object into the dictionary so that it can be used later
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

	main(gridSize,mineCount)
