#turtle modulunu ekledik
import turtle
#kalem rengi beyaz
turtle.color("white")
#arka plan rengi yesil
turtle.bgcolor("green")

#dongu baslıyor x:0..4 (4 dahil degil)
for x in range(4):
    #ekrana x degerini yaz
    turtle.write("x:"+str(x)) #x normalde integerdı onu str yaptık
    #100 adim git
    turtle.fd(100)
    #sola doksan derece git
    turtle.left(90)
