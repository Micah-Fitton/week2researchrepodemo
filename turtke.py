from turtle import *
import random
#i = random.randint(-100,100)


pensize(2)

def triangle():
    for loop in range(500):
        
        speed(0)
        forward(loop)
        left(100)

triangle()
done()