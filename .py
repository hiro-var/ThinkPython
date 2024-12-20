#fdは長さで、ltは角度？
#thinkpythonに記載されているものでは起動しないため、自分で修正
import turtle

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

bob = turtle.Turtle()
square(bob)

turtle.done()
