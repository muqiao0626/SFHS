# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 08:27:09 2015

@author: perona
"""

import random
import turtle

N_TURTLES = random.randint(1,10)

turtle_list = []
for i in range(N_TURTLES):
    t = turtle.Pen()
    t.shape("turtle")
    t.up()
    turtle_list.append(t)

prob_return = 0.05 # prob. that on a given step the turtle wishes to go home
prob_egg = 0.01
prob_death = 0.02
n_steps = 10000

## useful functions

# lay egg
def lay_egg(t):
    t.down()
    t.begin_fill()
    t.circle(4) # this is the egg
    t.end_fill()
    t.up()
    
# move function
def turtle_step(t):
    go_home = random.random()<prob_return # decide whether to go home

#    if t.distance(0,0) > 400: # if far from home, then go back
    if go_home:
        angle = t.towards(0,0) # compute home direction
#        print(x,angle)
        t.setheading(angle) # point turtle towards home

    # change current direction a bit
    angle = 60*(random.random()-0.5) 
    t.left(angle)

    # take a steps of variable length
    step = 5+20*random.random()
    t.forward(step)
    
    
##
# main program - let the turtles go around
for x in range(n_steps):
    # visit each turtle in turn
    for i in range(N_TURTLES):
        t = turtle_list[i]
        turtle_step(t)
        # every now and then lay an egg
        if random.random()<prob_egg:
            lay_egg(t)

    # kill one of the turtles from now and then
    if random.random()<(prob_death*N_TURTLES):
        i = random.randint(0,N_TURTLES-1)
        turtle_list[i].color("red") # dead turtles turn red
        turtle_list.pop(i) # take the dead turtle out of the list
        N_TURTLES= N_TURTLES-1
        if N_TURTLES == 0: # stop program if no more turtles
            print("all dead!!")
            break
        
    
