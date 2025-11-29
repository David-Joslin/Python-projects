import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
pen.speed(0)
turtle.colormode(255)
for i in range(20):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    pen.up()
    pen.goto(x,y)
    pen.down()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pen.color(r,g,b)

    i = 36
    while i > 0:
        i = i - 1
        move = random.randint(30,80)
        pen.forward(move)
        pen.backward(move)
        pen.right(10)

turtle.done()






