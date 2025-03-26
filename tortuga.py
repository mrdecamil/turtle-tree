
import turtle


def treet(t, branch_lenght, branches, angle, order, colors):
  color_id = order % len(colors)
  if order > 0:
    t.color(colors[color_id])
    t.forward(branch_lenght)
    #rama izquierda
    #if branches % 2 == 0:
    angle_pow = (branches / 2) -.5
    #else:
      #angle_pow = math.trunc(branches / 2)
    t.left(angle*angle_pow)
    treet(t, branch_lenght * .7, branches, angle, order-1, colors)
    t.color(colors[color_id])
    for i in range(1,branches):
      #rama centro
      t.right(angle)
      treet(t, branch_lenght * .7, branches, angle, order-1, colors)
      t.color(colors[color_id])
    #rama derecha
    #t.right(angle)
    #treet(t, branch_lenght * .7, angle, order-1, colors)
    #vuelve al centro
    t.left(angle*angle_pow)
    t.backward(branch_lenght)
  else:
    t.color(colors[color_id])
    t.stamp()
    t.color(colors[color_id])
window = turtle.Screen()
window.bgcolor("black") 

colors = ["purple", "blue", "cyan", "white"]
t = turtle.Turtle() 
t.speed (0)
t.left(90)
#dinuja el arbol(orden5, longitud 100, angulo 30)
treet(t, 80, 3, 30, 7, colors)
window.mainloop()