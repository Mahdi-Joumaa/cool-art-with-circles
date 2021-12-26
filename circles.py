import turtle
from turtle import *
import time

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range (20):
    for colors in ['red', 'white', 'cyan', 'blue', 'green', 'pink', 'purple', 'orange', 'aqua']:
                    turtle.color(colors)
                    turtle.circle(100)
                    turtle.left(2)
hideturtle()
