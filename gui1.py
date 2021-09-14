# imports
import time
from tkinter import *
def onClick(e):
	Label(text='Hello World'+e).grid(row=1,column=0)
e=input('Enter smthng')
# Create Tk object
window = Tk(className='Minesweeper')
b1=Button(text='Click Me')
b1.grid(row=0,column=0)
print(b1.text)
mainloop()
