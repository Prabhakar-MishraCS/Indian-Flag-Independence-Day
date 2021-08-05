import turtle
import time
from pygame import mixer

# Main Screen
wn = turtle.Screen()
wn.title("Independence day")
wn.setup(width = 1365, height = 697)
wn.bgcolor("White")
#wn.tracer(0)

pygame.init()
mixer.init()
mixer.music.load('anthem.wav')
mixer.music.play()

time.sleep(7)
wn.addshape('fl.gif')
t = turtle.Turtle()
t.penup()
t.speed(10)
t.shape('fl.gif')
t.goto(1364,0)
t.pendown()
t.hideturtle()

#turtle.bgpic("flag.gif")


# Basement
flag = turtle.Turtle()
flag.speed(8)
flag.color("Black")
flag.pensize(5)
flag.penup()
flag.goto(-450, -330)
flag.pendown()
flag.fillcolor("Brown")
flag.begin_fill()
flag.speed(8)

for i in range(4):
    flag.left(90)
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(90)
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(180)
    flag.fd(60)
flag.end_fill()
flag.right(180)
flag.fd(240)
flag.right(90)
flag.fd(30)
flag.right(90)
flag.fd(30)
flag.left(90)
flag.begin_fill()
flag.speed(8)

for j in range(3):
    flag.fd(30)
    flag.right(90)
    flag.fd(60)
    flag.right(90)
    flag.fd(30)
    flag.right(180)
flag.end_fill()
flag.left(90)
flag.fd(180)
flag.right(90)
flag.fd(30)
flag.right(90)
flag.fd(85)
flag.left(90)
flag.color("Black")
flag.begin_fill()

# Long stick
flag.speed(8)

flag.fd(550)
flag.right(90)
flag.fd(5)
flag.right(90)
flag.fd(550)
flag.end_fill()
flag.right(180)
flag.fd(550)

# Flag
flag.speed(9)
flag.fillcolor("Orange")
flag.pensize(3)
flag.begin_fill()
flag.right(45)

flag.fillcolor("orange")

# Line 1
flag.begin_fill()
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.right(135)
flag.fd(45)
flag.left(135)
flag.right(180)
flag.speed(9)

# Line 1 Reverse

for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.end_fill()
flag.left(45)
flag.fd(45)
flag.right(180)
flag.right(45)
flag.speed(9)

# Line 2

flag.fillcolor("Green")
flag.speed(10)
flag.begin_fill()
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.speed(9)

flag.right(135)
flag.fd(45)
flag.left(135)
flag.right(180)

# Line 2 Reverse
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(100):
    flag.fd(1.5)
    flag.left(1)
flag.end_fill()
flag.left(45)
flag.right(180)
flag.fd(45)
flag.penup()
flag.right(45)
flag.speed(5)
for i in range(100):
    flag.fd(1.5)
    flag.right(1)
for i in range(8):
    flag.fd(1.5)
    flag.left(1)
flag.pendown()

# Circle
flag.setheading(0)
flag.left(45)
flag.fd(5)
flag.setheading(0)
flag.pensize(3)
flag.color("Blue")
flag.circle(15)

flag.penup()
flag.left(90)
flag.fd(15)
flag.right(90)
flag.pendown()

# Ashoka Chakra
flag.pensize(1)
for i in range(24):
    flag.forward(15)
    flag.bk(15)
    flag.left(15)
flag.hideturtle()

# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(3)
pen.color("Red")
pen.pensize(10)
pen.penup()
pen.goto(250, 0)
pen.pendown()
#time.sleep(3)
pen.write("PrabhuCS Wishing You All..", font = ("Helvetica",30, "bold"), align = "center")
pen.penup()
time.sleep(2)
pen.color("green")
pen.goto(200, -100)
pen.pendown()
pen.write("A VERY HAPPY INDEPENDENCE DAY 2021 :)", font = ("chiller", 45, "bold"), align = "center")
time .sleep(5)
pen.hideturtle()