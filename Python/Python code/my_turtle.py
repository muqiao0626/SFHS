# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:59:45 2015

@author: perona
"""
import turtle

class Fertile_Turtle(turtle.Pen):
    def __init__(self):
        turtle.Pen.__init__(self)
        
    def lay_egg(self):
         self.down()
         self.begin_fill()
         self.circle(4) # this is the egg
         self.end_fill()
         self.up()
         return self.pos()
         
