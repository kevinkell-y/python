# 04. ColorSquareSpiral.py

import turtle

turtle.bgcolor("black")
t = turtle.Pen()

colors = ["red", "yellow", "blue", "green"]

for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
