import turtle

def square(t):
    for i in range(8):
        t.fd(100)
        t.lt(45)

bob = turtle.Turtle()  
square(bob)            

turtle.done()          
