#!/usr/bin/env python

from Tkinter import *
import sys
from random import randint

#setup grid frame
#setup grid frame
class Grid(object):
    def __init__ (self,master=None,width=1000,height=800,grid_width=20,offset=10): 
		self.height = height
		self.width = width
		self.grid_width = grid_width
		self.grid_x = width / grid_width 
		self.grid_y = height / grid_width 
		self.offset = offset
		self.canvas = Canvas(master,width = self.width - self.offset, height = self.height -
		self.offset,bg ='grey')
		self.canvas.pack (side=LEFT)                #setup canvas position 
		self.list()
    def draw(self, position,color):             #setup every element
		x_axis = position[0] * self.grid_width + self.offset
		y_axis = position[1] * self.grid_width + self.offset
		self.canvas.create_rectangle (x_axis,y_axis, x_axis + self.offset, y_axis + self.offset,fill = color,outline='grey')
    def list(self):         #create every small element
		list=[]
		for x_axis in range (0, self.grid_x-1):
		    for y_axis in range (0, self.grid_y-1):
				list.append((x_axis,y_axis))
		self.list = list

class Apple (object):
    def __init__ (self,Grid):
	self.grid = Grid
	self.position()
    def position(self):		    #apple position
    	x = randint (0,self.grid.grid_x-1)
	y = randint (0,self.grid.grid_y-1)
	print(self.grid.offset)
	self.pos = (x,y)
	print(self.pos)
    def showup(self):		    #display apple
	self.grid.draw(self.pos,bg = 'green')

class speed(object):
    def __init__ (self,master =None):
	self.frame =Frame(master,width=300,height=200)
	self.frame.pack()
	label = Label(self.frame,text = 'Snake Game',font=("Purisa",40),fg = 'Red')
	label.pack(side=TOP)
	label2 = Label(self.frame, text = 'Xuyu Duan')
	label2.pack(expand = 'Yes',side=TOP)
	label3 = Label (self.frame , text = 'Dong Wang')
	label3.pack(side = TOP)
	label4 = Label (self.frame , text = 'Sheng Wei')
	label4.pack(side = TOP)
	button1 = Button(self.frame,text='slow',command=self.Return)
	button1.pack(side=BOTTOM)
	button2 = Button(self.frame,text='Midium',command = self.Return2)
	button2.pack(side=BOTTOM)
	button3 = Button(self.frame,text = 'Fast',command = self.Return3)
	button3.pack(side = BOTTOM)
	self.spe =100
    def Return(self):
	self.spe = 300
	self.frame.destroy()

    def Return2(self):
	self.spe = 400
	print(self.spe)
	self.frame.destroy()
    def Return3(self):
	self.spe = 700
	self.frame.destroy()	
	

class Snake(object):
    def __init__ (self,Grid):
	self.grid = Grid
	self.apple = Apple(self.grid)
	self.snake_length = 3
	self.snake = [(12,6),(12,7),(12,8)] 
    def display (self):
	for (x,y) in self.snake
	    self.grid.draw((x,y),'blue')
	pos = self.snake[0]
	self.grid.draw(pos,'dark')
    def isAvaliable(self):
	for i in self.grid.list:
	    if i not in self.snake [1: ]:
		return True
    def display_apple(self):
	while (1):
	    num = self.apple.position()
	    if num not in self.snake:    
		break
	self.apple.showup()
    def dir_change (self,direction):
	self.direction = direction
    def move(self):
	

if __name__ == "__main__":
    root = Tk()
    #b=speed(root)
    #c = Snake(root)
    #c.display()
    Grid(root)
    Apple(root)
    #a=b.spe
    #print(a)
    #GApple(root)
    root.mainloop()
