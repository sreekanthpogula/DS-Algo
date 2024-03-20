import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length):
    """Draws the square using the length as an argument"""
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 200)

turtle.mainloop()


import turtle
bob = turtle.Turtle()
print(bob)

def ploygon(t, length, n):
    """Draws the polygon with the n sides"""
    for i in range(n):
        t.fd(length)
        angle = 360/n
        t.lt(angle)

ploygon(bob, 200
, 5)

turtle.mainloop()



