import turtle
import random
import tortuga

def koch(t, order, size):
  if order == 0:
    t.forward(size)
  else:
    koch(t, order-1, size/3)
    t.left(90)
    koch(t, order-1, size/3)
    t.right(120)
    koch(t, order-1, size/3)
    t.left(90)
    koch(t, order-1, size/3)


window = turtle.Screen()
window.bgcolor("white")

colors = ("blue", "red", "white", "purple")
t = turtle.Turtle()
t.speed(0)
# t.color("color string: %s" % str(colors)")")
tortuga.treet(t, 80, 3, 30, 3, colors)

t.penup()
t.goto(-150, 90)
t.pendown()

for i in range(6):
  koch(t, 4, 300)
  t.right(120)
