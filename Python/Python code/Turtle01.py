import turtle

t = turtle.Pen()

for tau in range(0,10):
    t.forward(20)
    t.left(88)
    t.forward(200-tau)
    t.left(92)
    t.forward(50)
    t.left(90)
    t.forward(210+tau)
    t.left(90)
