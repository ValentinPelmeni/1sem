import turtle
from random import random
number_of_turtles = 10
dt = 0.01
a = [turtle.Turtle() for i in range(number_of_turtles)]
Vx = [random()*100 for i in range(number_of_turtles) ]
Vy = [random()*100 for i in range(number_of_turtles) ]
x = [0 for i in range(number_of_turtles) ]
y = [0 for i in range(number_of_turtles) ]
for z in range(number_of_turtles):
    a[z-1].penup()
for i in range(10000):
    for z in range(number_of_turtles):
        x[z-1] = x[z-1] + Vx[z-1]*dt
        y[z-1] = y[z-1] + Vy[z-1]*dt
        a[z-1].goto(x[z-1], y[z-1])
        if x[z-1] < -200 :
            Vx[z-1]=-Vx[z-1]
        if y[z-1] < -200 :
            Vy[z-1]=-Vy[z-1]
        if x[z-1] > 200 :
            Vx[z-1]=-Vx[z-1]
        if y[z-1] > 200 :
            Vy[z-1]=-Vy[z-1]
        
        