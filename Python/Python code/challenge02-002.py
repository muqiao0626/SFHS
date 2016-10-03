import random
import turtle

t1 = turtle.Pen()
t1.shape("turtle")
t1.color("red")
t1.up()

t2 = turtle.Pen()
t2.shape("turtle")
t2.up()

prob_return = 0.05 # prob. that on a given step the turtle wishes to go home
prob_egg = 0.05;
n_steps = 10000

## useful functions

# lay egg
def lay_egg(t):
    t.down()
    t.begin_fill()
    t.circle(4) # this is the egg
    t.end_fill()
    t.up()
    
# move   
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
    turtle_step(t1)
    turtle_step(t2)

    # every now and then lay an egg
    if random.random()<prob_egg:
        lay_egg(t2)
         
    if random.random()<prob_egg:
        lay_egg(t1)
 
    
