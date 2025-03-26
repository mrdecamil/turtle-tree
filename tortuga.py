python

import turtle

def treet(t, branch_lenght, angle, order, colors):
  if order > 0:
    t.color(colors [order % len(colors)])
    t.forward(branch_lenght)
    #rama izquierda
    t.left(angle)
    treet(t, branch_lenght * .6, angle, order-1, colors)
    #rama centro
    t.right(angle)
    treet(t, branch_lenght * .6, angle, order-1, colors)
    #rama derecha
    t.right(angle)
    treet(t, branch_lenght * .6, angle, order-1, colors)
    #vuelve al centro
    t.left(angle)
    t.backward(branch_lenght)
  else:
    t.color("blue")
    t.stamp()
    t.color("green")
window = turtle.Screen()
window.bgcolor("black") 

colors = ["purple", "blue", "cyan", "white"]
t = turtle.Turtle() 
t.speed (2)
t.left(90)
#dinuja el arbol(orden5, longitud 100, angulo 30)
treet(t, 80, 45, 5, colors)
window.mainloop()