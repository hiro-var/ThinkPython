#遅いため改善点があるかも
import turtle

def cercle(t):
    for i in range(360):
        t.fd(1)
        t.lt(1)

bob = turtle.Turtle()  
cercle(bob)            

turtle.done()          
