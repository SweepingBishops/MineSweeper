#!/usr/bin/python3.8
from functools import partial
from time import time
from platform import system
from PIL import Image, ImageTk
import tkinter
import endScreen
from plantMines import plantMines, identifyNeighbouringSquares


def main(gridSize,mineCount):
    ###Global variables###
    result = None
    firstClickFlag, gameover = True, False
    tileIdentity, minePositions , squareValues = {}, {}, {}
    startTime, endTime, clickedSquares = 0,0,0
    if system() == 'Linux':
        buttonHeight = 2
        buttonWidth = 4
        buttonHeightWithImage = 46
        buttonWidthWithImage = 62
    elif system() == 'Windows':
        buttonHeight = 2
        buttonWidth = 5
        buttonHeightWithImage = 46
        buttonWidthWithImage = 49
    else:
        print(f'This program has not been tested on {system()}!')
        buttonHeight = 2
        buttonWidth = 4
        buttonHeightWithImage = 46
        buttonWidthWithImage = 62

    class tile():   #creating a class for a minesweeper tile
        def __init__(self,mainWindow,xPos,yPos):
            self.xPos = xPos
            self.yPos = yPos
            self.leftClicked, self.rightClicked = False, False    #flags to check if the tile has been clicked
            self.button = tkinter.Button(mainWindow, disabledforeground='black', height=buttonHeight, width=buttonWidth)
            self.button.grid(row=xPos, column=yPos)
            self.button.bind("<Button-1>", self.leftClick)   #sets commands for left and right clicks
            self.button.bind("<Button-3>", self.rightClick)

        def leftClick(self,event=None):
            nonlocal result, gameover, firstClickFlag, clickedSquares, minePositions, squareValues, startTime, endTime
            if self.rightClicked or self.leftClicked or gameover:
                return None
            self.leftClicked = True
            if firstClickFlag:  #on the first left click of the game mines are planted
                firstClickFlag = False
                minePositions, squareValues = plantMines(self.xPos, self.yPos, gridSize, mineCount)
                startTime = time()  #reads the time when the game is started

            if (self.xPos,self.yPos) not in minePositions:  #if the clicked tile is not a mine it is shown as green
                self.button.configure(text=squareValues[(self.xPos,self.yPos)], bg='green', activebackground='green')
                clickedSquares += 1 #if the number of clicked squares is equal to non-mine squares game is won. checked below
            else:
                for mine in minePositions:  #game is over when a mine is clicked
                    tileIdentity[mine].button.configure(height=buttonHeightWithImage, width=buttonWidthWithImage, bg='orange', activebackground='orange', image=mineImage)
                self.button.configure(height=buttonHeightWithImage, width=buttonWidthWithImage, bg='red', activebackground='red', image=mineImage)
                gameover = True
                if __name__ != '__main__':  #calls the game end screen
                    endScreen.display('You Lost :(',None)
                return
            if clickedSquares == (gridSize**2 - mineCount): #checks if the game is won
                endTime = time()    #the time when the game ends
                gameover = True
                for mine in minePositions:  #displays all mines as flags
                    tileIdentity[mine].button.configure(height=buttonHeightWithImage, width=buttonWidthWithImage, image=flagImage)

                score = round(endTime - startTime)
                hours = score//3600
                score %= 3600
                minutes = score//60
                seconds = score%60
                result = 'You Won!\n%02d:%02d:%02d'%(hours,minutes,seconds)
                if __name__ != '__main__':  #calls game end screen
                    endScreen.display(result, gridSize)
                return None

            if squareValues[(self.xPos,self.yPos)] == None: #opens all neighbouring tile if the current tile has value zero(game rule)
                neighbouringSquares = identifyNeighbouringSquares(self.xPos,self.yPos,gridSize)
                for neighbouringSquare in neighbouringSquares:
                    tileIdentity[neighbouringSquare].leftClick()


        def rightClick(self,event=None):
            if not self.rightClicked and not self.leftClicked:  #shows flag if not already flagged or left clicked
                self.rightClicked = True
                self.button.configure(height=buttonHeightWithImage, width=buttonWidthWithImage, image=flagImage)
            else:   #removes flag
                self.rightClicked = False
                self.button.configure(height=buttonHeight, width=buttonWidth, image='')
    #creating main window
    global mainWindow
    mainWindow = tkinter.Tk(className='Minesweeper')
    mainWindow.option_add('*Font','Consolas 12')
    #images for the mine and the flag
    flagImage = ImageTk.PhotoImage(Image.open('flag.png').resize((50,50)))
    mineImage = ImageTk.PhotoImage(Image.open('mine.png').resize((50,50)))

    for i in range(gridSize):
        for j in range(gridSize):
            #creates a tile object
            button = tile(mainWindow,i,j)
            tileIdentity[(i,j)] = button    #adds the object into the dictionary with key as its x and y coordinates so that it can be used later
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
