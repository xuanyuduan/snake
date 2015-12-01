#!/usr/bin/env python

from Tkinter import *
import sys
from random import randint


#initial message
class Init(object):
    def __init__ (self,master =None):
        self.frame =Frame(master,width=300,height=780,bg='black')
	self.frame.propagate (False)
        self.frame.pack(side=LEFT,padx =2)
        label = Label(self.frame,text = 'Snake Game',font=("Purisa",40),fg = 'Red',bg='black')
        
	label.pack(side=TOP)#,expand ='Yes',fill=Y)
        empty = Label (self.frame,bg ='black')
	empty.pack(side=TOP)
	label2 = Label(self.frame, text = 'Xuyu Duan   ',fg = 'white',bg = 'black')
        label2.pack(side=TOP, anchor = E)#,expand ='Yes',fill= Y)
        label3 = Label (self.frame , text = 'Dong Wang   ',fg = 'white',bg = 'black')
        label3.pack(side = TOP,anchor = E)#,expand ='Yes',fill = Y)
        label4 = Label (self.frame , text = 'Sheng Wei   ',fg = 'white',bg = 'black')
        label4.pack(side = TOP ,anchor = E)#,expand='Yes',fill=Y)
	label5 = Label (self.frame,text ="<Press s to start>",fg = 'red',bg ='black',)
	label5.pack(side=TOP)
	var =StringVar()
	message = Message (self.frame,textvariable=var,bg= 'black',fg='white',width=300)
	var.set("How to play:\n	    Pause : p\n	    Direction: direction key")
	message.pack(side=TOP)
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
    	x = randint (1,self.grid.grid_x-2)
	y = randint (1,self.grid.grid_y-2)
	print(self.grid.offset)
	self.pos = (x,y)
	print(self.pos)
    def showup(self):		    #display apple
	self.grid.draw(self.pos,bg = 'green')

class Snake(object):
    def __init__ (self,Grid):
	self.grid = Grid
	self.apple = Apple(self.grid)
	self.snake = [(12,6),(12,7)] 
	self.status = [0,1]   # 0 -> stop 1->run
	self.score = 0
	self.isOver = False
	self.direction = 'Right'
    def display (self):
	for (x,y) in self.snake:
	    self.grid.draw((x,y),'blue')
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
	if direction == 'Up' and not self.privious  == 'Down':
            self.privious = direction 
            self.direction = direction
        if direction == 'Down'and not self.privious  == 'Up':
            self.privious = direction 
            self.direction = direction
        if direction == 'Left' and not self.privious  == 'Right':
            self.privious = direction 
            self.direction = direction
        if direction == 'Right' and not self.privious  == 'Left':
            self.privious = direction
            self.direction = direction
    def move(self):
		
	
class Game(Frame):
    def __init__ (master =None,*args,**kwargs):
	Frame.__init__(self,master)
	self.master = master
	self.grid = Grid(master,*args,**kwargs)
	self.snake = Snake(self.grid)
	self.isStart = False
	self.bind_all("<KeyRelease>", self.key_release)
    def run(self):	
	if self.isStart is True:
	    if self.status is 1:
			self.snake.move()
	    if self.snake.isOver is True:
			sys.exit()
    def key_release(self, event):
        key = event.keysym
	direc = {'Up','Down','Left','Right'}
        if key in direc:   
	    print(key)
            self.snake.change_direction(key)
            self.snake.move()
        elif key == 'p':
            self.snake.status.reverse()
	elif key = 'Return':
	    self.isStart = True 

if __name__ == "__main__":
    root = Tk()
    #b=speed(root)
    #c = Snake(root)
    #c.display()
    Grid(root)
    Init(root)
    #Apple(root)
    #a=b.spe
    #print(a)
    #GApple(root)
    root.mainloop()
