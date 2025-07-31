import turtle
from random import randint as r

turtle.getscreen()
t = turtle.Turtle()
t.speed(200)
turtle.colormode(255)
t.pencolor((0, 20, 100))
a = int(input())

c = 360 / a

for i in range(0, a):
    t.pencolor((r(0, 255), r(0, 255), r(0, 255)))
    x = r(30, 200)
    t.fd(x)
    t.bk(x)
    t.left(c)
