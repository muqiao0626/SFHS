import random
import turtle

t = turtle.Pen()
t.shape("turtle")
home_size = 200

# draw the turtle's home
t.right(90)
t.forward(home_size)
t.left(90)
t.circle(home_size)

for x in range(10000):

     # if turtle too far from home - point it back to home
    if t.distance(0,0) > home_size:
        angle = t.towards(0,0)
        t.setheading(angle)
        
    step = 20*random.random() # length of step the turtle takes
    angle = 30*(random.random()-0.5) # how much the turtle turns
    t.left(angle)
    t.forward(step)
    
