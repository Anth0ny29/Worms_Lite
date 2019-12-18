from tkinter import *
from math import pi, sin ,cos

class Roquette(object):
	def __init__(self,parent,x,y,coul):
		self.parent=parent
		self.x=x
		self.y=y
		r=5
		self.r=self.parent.create_oval(self.x-r,self.y-r,self.x+r,self.y+r,fill=coul)

	def destroy(self):
		self.parent.delete(self.r)
		
