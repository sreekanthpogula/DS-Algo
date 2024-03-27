from __future__ import print_function, division

import turtle


def draw_spiral(t, n, length, a, b):
    """Draws an Archimedian spiral starting at the origin.
    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


bob = turtle.Turtle()
draw_spiral(bob, n=1000, length=1, a=0.1, b=0.0002)

turtle.mainloop()