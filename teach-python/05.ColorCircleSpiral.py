# 04. ColorCircleSpiral.py

import turtle

turtle.bgcolor("black")
t = turtle.Pen()

colors = ["red", "yellow", "blue", "green"]

for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)
