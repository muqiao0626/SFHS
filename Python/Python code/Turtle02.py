import turtle

t = turtle.Pen()

L= 1000
SIDES = 100

t.penup()
t.right(90)
t.forward(L/6.28)
t.left(90)
t.pendown()

t.speed(1000)
t.pensize(3)


for tau in range(0,5):
    for s in range(0,SIDES):
        t.forward(L/SIDES+50*tau/SIDES)
        t.left(360/SIDES)
