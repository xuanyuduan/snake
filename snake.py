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
    def list(self):
	list=[]
	for x_axis in range (0, self.grid_x-1):
	    for y_axis in range (0, self.grid_y-1):
		list.append((x_axis,y_axis))
	self.list = list

class Apple (object):
    def __init__ (self,Grid):
	self.grid = Grid
	self.setup()
    def position(self):
    	x = randint (0,self.grid.x_axis-1)
	y = randint (0,self.grid.y_axis-1)
	self.pos = (x,y)
    def showup(self):
	self.grid.setup(self.pos,bg = 'green')


if __name__ == "__main__":
    root = Tk()
    Grid(root)
    root.mainloop()
