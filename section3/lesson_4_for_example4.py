import turtle
turtle.pensize(3)
turtle.color("red")
turtle.bgcolor("blue")

for x in range(36):
    turtle.home()
    turtle.left(x*10)
    turtle.circle(100)
