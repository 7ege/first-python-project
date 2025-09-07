import turtle        #turtle kutuphanesini dahil et
turtle.speed(0)
turtle.color("red")

for x in range(36):    #36 kere
    turtle.left(10)#10 derece don
    if (x%4==0):
        turtle.begin_fill()

    for y in range(4):  #bir adet kare cizer
        turtle.fd(100)
        turtle.left(90)
    turtle.end_fill()
