import math 
from turtle import *
def hearta(b):
    return 15*math.sin(b)**3

def heartb(b):
    return 11*math.cos(b)-5*\
    math.cos(2*b)-\
    math.cos(3*b)-\
    math.cos(4*b)

speed(9000)
bgcolor("black")

for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()