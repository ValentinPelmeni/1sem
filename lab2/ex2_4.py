import turtle as t
import numpy as np
import random as rd
t.speed(100)
ay = -70
Vx = 100
Vy = 50
dt = 0.001
x = 0
y = 0
for i in range(100000):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y<0 :
        Vy= -Vy
    t.goto(x, y)