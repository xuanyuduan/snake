#!/usr/bin/env python

from Tkinter import *
import sys
from random import randint

#setup grid frame
class Grid(object):
    def __init__ (self,master=None,width=1000,height=800,grid_width=10,offset=20): 
	self.height = height
	self.width = width
	self.grid_x = width / grid_width 
	self.grid_y = height / grid_width 
	self.offset = offset
	self.canvas = Canvas(master,width = self.width+2*self.offset, height = self.height +
	2*self.offset,bg ='white')
	self.canvas.pack (side=LEFT)			    #setup canvas position 
	self.list()
    def setup(self, position,color):			    #setup every element
	x_axis = position[0] * self.grid_width + self.offset
	y_axis = position[0] * self.grid_width + self.offset
	self.canvas.element (x_axis,y_axis, x_axis + self.offset, y_axis + self.offset, fill =
	color,bg='white')
    def list(self):		    #create every small element
	list=[]
	for x_axis in range (0, self.grid_x-1):
	    for y_axis in range (0, self.grid_y-1):
		list.append((x_axis,y_axis))
	self.list = list

class Apple (object):
    def __init__ (self,Grid):
	self.grid = Grid
	self.setup()
    def position(self):		    #apple position
    	x = randint (0,self.grid.x_axis-1)
	y = randint (0,self.grid.y_axis-1)
	self.pos = (x,y)
    def showup(self):		    #display apple
	self.grid.setup(self.pos,bg = 'green')

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
	self.snake_length = 3
	self.snake = [(12,6),(12,7),(12,8)] 
    def display (self):
	self.grid.setup(self.snake[0],bg='green')


if __name__ == "__main__":
    root = Tk()
    b=speed(root)
    Grid(root)
    a=b.spe
    print(a)
    root.mainloop()
