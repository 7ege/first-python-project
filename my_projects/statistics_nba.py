sayi=0
ribaund=0
asist=0

while True:
    print("NBA ALL STAR HOSGELDINIZ")
    oyuncu = input("Oyuncu seciniz: Lebron or Curry ")




    points=int(input("Oyuncu kac sayi atti: "))
    rib=int(input("Kac ribaund aldi: "))
    asi=int(input("Kac asist yapti: "))


    sayi=sayi+points
    ribaund=ribaund+rib
    asist=asist+asi


    if points >= 25 and rib >= 6 and asi >= 5:
        print(oyuncu, "Mukemmel oynamistir ve istatistikler:",
              "Toplam sayi:", sayi,
              "Toplam Ribaund:", ribaund,
              "Toplam Asist:", asist, "kadardir.")

    else:
        print(oyuncu, "Vasat kalmistir ve istatistikler:",
              "Toplam sayi:", sayi,
              "Toplam Ribaund:", ribaund,
              "Toplam Asist:", asist, "kadardir.")









