# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:25:49 2015

@author: perona
"""

import turtle
import random

turtle.clearscreen()
t = turtle.Pen()
t.home()

def box(n,sz):
    for i in range(n):
        t.forward(3.14*sz/n)
        t.left(360/n)
        
def star(n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(180-180/n)
        

for k in range(10):
    n = random.randint(3,8)
    x = 400*random.random()-200
    y = 400*random.random()-200
    sz = 50+100*random.random()
    t.up()
    t.goto(x,y)
    t.down()
    box(n,sz)
    



#turtle.done()