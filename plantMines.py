#imports
from random import *
from tkinter import *

def plantMines(gridSize,mineCount):		#function for intialising mine positions
	minePositions = set()
	while len(minePositions) < mineCount:	#uses set to ensure that the values are unique; while loop is used to ensure that the number of mines are correct
		minePositions.add((randint(0,gridSize - 1),randint(0,gridSize - 1)))	#uses random for deciding where to put mines
	squareValues = {}	#the value shown on each square when it is clicked
	for i in range(gridSize):
		for j in range(gridSize):
			squareValues[ (i,j) ] = 0	#initalises a dictionary with all zeroes

	neighbouringSquares = []
	for i , j  in minePositions:
		squareValues[ (i,j) ] = 'mine'
		neighbouringSquares =[				#identifies the neighbouring squares of the square with index (i,j)
		( i-1 , j-1 ) , ( i , j-1 ) , ( i+1 , j-1 ),
		( i-1 , j )   ,               ( i+1 , j ),
		( i-1 , j+1 ) , ( i , j+1 ) , ( i+1 , j+1 )]
		for neighbouringSquare in neighbouringSquares:
			if 0 <= neighbouringSquare[0] < gridSize and 0 <= neighbouringSquare[1] < gridSize and (neighbouringSquare[0],neighbouringSquare[1]) not in minePositions:	#checks if the square is whithin the grid and not a mine
				squareValues[neighbouringSquare] += 1
	return minePositions , squareValues
