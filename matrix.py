#imports
from random import *
from tkinter import *

#initialising variables
rowCount = int(input('Enter number of rows: '))
columnCount = int(input('Enter number of columns: '))
mineCount = int(input('Enter number of mines: '))
minePosition = []
play = True

def plantMines(rowCount,columnCount,mineCount):		#function for intialising mine positions
	for i in range(mineCount):
		minePosition.append((randint(1,rowCount),randint(1,columnCount)))	#uses random for deciding where to put mines
	'''remember to fix multiple mines in one square'''	
plantMines(rowCount, columnCount, mineCount)
print(minePosition)
def onClick(square):
	if square in minePosition:
		print('You lost:(')
		sleep(2)
		exit()
	else:
		pass #openSquare()
while play:
	square = eval(input('Enter a square to click: '))
	onClick(square)
