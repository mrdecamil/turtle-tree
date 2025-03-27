""" Build a fractal tree with turtle"""
import turtle


def treet(turtle_pointer: turtle,
          branch_lenght: int,
          branches: int,
          angle: int,
          order: int = 1,
          colors_list: list = None):
    """ Recursive function to draw tree.
        take angles, branch quanty and level of recursiviti
    """
    if colors_list is None:
        colors_list = ["Green", "Blue"]
    color_id = order % len(colors_list)
    turtle_pointer.pendown()
    if order > 0:
        turtle_pointer.color(colors_list[color_id])
        turtle_pointer.forward(branch_lenght)
        angle_pow = (branches / 2) - .5
        turtle_pointer.left(angle*angle_pow)
        treet(turtle_pointer,
              branch_lenght * .7,
              branches,
              angle,
              order-1,
              colors_list
            )
        for i in range(1, branches):
            # draw the branches
            turtle_pointer.right(angle)
            treet(turtle_pointer, branch_lenght * .7, branches, angle, order-1, colors_list)
        turtle_pointer.left(angle*angle_pow)
        turtle_pointer.backward(branch_lenght)
    else:
        turtle_pointer.color(colors_list[color_id])
        turtle_pointer.stamp()
        turtle_pointer.penup()


if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("black")

    colors = ["purple", "blue", "cyan", "white"]
    t = turtle.Turtle()
    t.speed(0)

    t.left(90)
    # dibuja el arbol(orden5, longitud 100, angulo 30)
    treet(t, 80, 3, 30, 3, colors)
    window.mainloop()
