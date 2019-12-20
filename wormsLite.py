from tkinter import *
from bazooka import *
from roquette import *


class Worms(Frame):
    def create_roquette1(self):
        self.roquette1=Roquette(self.can,self.b1.x2,self.b1.y2,'red')
        

    def create_roquette2(self):
        self.roquette2=Roquette(self.can,self.b2.x2,self.b2.y2,'green')

    def destroy_roquette1(self):
        self.roquette1.destroy()

    def destroy_roquette2(self):
        self.roquette2.destroy()

    def __init__(self):
        # Code pour tester sommairement la classe Bazouka :
        f = Tk()
        self.can = Canvas(f,width =500, height =250, bg ='ivory')
        self.can.pack(padx =10, pady =10)
        self.b1 = Bazooka(self.can, 50, 200)
        self.b2 = Bazooka(self.can, 400,200)
        s1 =Scale(f, label='hausse', from_=90, to=0, command=self.b1.orienter)
        s1.pack(side=LEFT, pady =5, padx =20)
        s1.set(0)                          # angle de tir initial
        s2 =Scale(f, label='hausse', from_=90, to=180, command=self.b2.orienter)
        s2.pack(side=RIGHT, pady =5, padx =20)
        s2.set(180)
        boutton_tir1=Button(f,text='tir',command=self.create_roquette1)
        boutton_tir1.pack(side=LEFT)
        boutton_tir2=Button(f,text='tir',command=self.create_roquette2)
        boutton_tir2.pack(side=RIGHT)
        boutton_Detruire1=Button(f,text='destroyR1',command=self.destroy_roquette1)
        boutton_Detruire1.pack(side=LEFT)
        boutton_Detruire1=Button(f,text='destroyR2',command=self.destroy_roquette2)
        boutton_Detruire1.pack(side=RIGHT)

        f.mainloop()

monJeu=Worms()
