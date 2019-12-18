from tkinter import *
from math import pi,sin,cos

class Roquette(object):
	def __init__(self,parent,x,y,coul):
                self.parent=parent
                self.x=x
                self.y=y
                self.r=self.parent.create_oval (self.x-5,self.y-5,self.x+5,self.y+5,fill=coul)
        #def destroy(self):
        #     self.parent.delete(self.r)
