import turtle
from random import randint as r

turtle.getscreen()
t = turtle.Turtle()
t.speed(200)
turtle.colormode(255)
t.pencolor((0, 20, 100))
a=int(input())

for i in range(0, a):
    for b in range(0,4):
        t.fd(100)
        t.left(90)
    t.left(360/a)    
