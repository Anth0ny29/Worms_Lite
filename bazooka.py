from tkinter import *
from math import pi, sin, cos

class Bazooka(object):
    """Petit canon graphique"""
    def __init__(self, boss, x, y):
        self.boss = boss
        # référence du canevas
        self.x1, self.y1 = x, y
        # axe de rotation du canon
        # dessiner la buse du canon, à l'horizontale pour commencer :
        self.lbu = 50
        # longueur de la buse
        self.x2, self.y2 = x + self.lbu, y
        self.buse = boss.create_line(self.x1, self.y1, self.x2, self.y2,
                                     width =10)
        # dessiner ensuite le corps du canon par-dessus :
        r = 15                      # rayon du cercle
        boss.create_oval(x-r, y-r, x+r, y+r, fill='blue', width =3)

    def orienter(self, angle):
            "choisir l'angle de tir du canon"
            # rem : le paramètre <angle> est reçu en tant que chaîne de car.
            # il faut le traduire en nombre réel, puis convertir en radians :
            self.angle = float(angle)*2*pi/360
            self.x2 = self.x1 + self.lbu*cos(self.angle)
            self.y2 = self.y1 - self.lbu*sin(self.angle)
            self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2)



