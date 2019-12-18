from tkinter import *
from bazooka import *
from roquette import *
# Code pour tester sommairement la classe Bazouka :
f = Tk()
can = Canvas(f,width =500, height =250, bg ='ivory')
can.pack(padx =10, pady =10)
b1 = Bazooka(can, 50, 200)
b2 = Bazooka(can, 400,200)
def create_roquette1():
    roquette1=Roquette(can,b1.x2,b1.y2,'red')





s1 =Scale(f, label='hausse', from_=90, to=0, command=b1.orienter)
s1.pack(side=LEFT, pady =5, padx =20)
s1.set(0)                          # angle de tir initial
s2 =Scale(f, label='hausse', from_=90, to=180, command=b2.orienter)
s2.pack(side=RIGHT, pady =7, padx =20)
s2.set(180)
boutton_tir=Button(f,text='tir',command=create_roquette1)
boutton_tir.pack(side=RIGHT)
f.mainloop()
