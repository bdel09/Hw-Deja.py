#Name: Benjamin Del Barrio
#Email: Benjamin.delbarrio31@myhunter.cuny.edu

import turtle
t = turtle.Turtle()
t.speed(0)  
for i in range(60, 112, 2):
    t.color("red")
    t.forward(i)
    t.left(45)
    t.color("blue")
    t.forward(i)
    t.right(90)
