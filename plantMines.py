#Imports
from random import randint

def identifyNeighbouringSquares(i,j,gridSize):		#identifies the neighbouring squares of the square with index (i,j)
	neighbouringSquares = []
	template =[				
		( i-1 , j-1 ) , ( i-1 , j ) , ( i-1 , j+1 ),
		( i , j-1 )   ,               ( i , j+1 ),
		( i+1 , j-1 ) , ( i+1 , j ) , ( i+1 , j+1 )]

	for x,y in template:
		if 0 <= x < gridSize and 0 <= y < gridSize:	#so that the square don't go outside the boundary
			neighbouringSquares.append((x,y))
	return neighbouringSquares

def plantMines(i,j,gridSize,mineCount):		#function to plant the mines and determine the square values
	minePositions = set()	#initiated as a set to prevent duplicates
	squareValues = {}
	while len(minePositions) < mineCount:
		x,y = randint(0,gridSize - 1),randint(0,gridSize - 1)	#uses random for deciding where to put mines
		if (x,y) != (i,j) and (x,y) not in identifyNeighbouringSquares(i, j, gridSize):	   #the square first clicked and its neighbours don't have mines
			minePositions.add( (x,y) )	

	for i in range(gridSize):
		for j in range(gridSize):
			squareValues[ (i,j) ] = 0	#initalises a dictionary with all values zero
	
	for i,j in minePositions:	#increments squareValue of all non-mine neighbouring squares
		squareValues[ (i,j) ] = 'mine'
		for neighbouringSquare in identifyNeighbouringSquares(i,j,gridSize):
			if neighbouringSquare not in minePositions:
				squareValues[neighbouringSquare] += 1
				
	for key in squareValues:
		if squareValues[key] == 0:
			squareValues[key] = None	#turns all zeroes into Nones for aesthetic reasons when displayed to the user
	return minePositions , squareValues
