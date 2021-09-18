from turtle import *
import time
speed(50)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b -= 1
time.sleep(5)
