while True:            
    print("1-Toplama\n 2-Çıkarma\n 3-Çarpma\n 4-Bölme\n 0-Çıkış")
    islem=int(input("İşlem seçiniz"))

    if islem==0:
        break
    
    elif islem==1:
        sayi1=int(input("1. Sayiyi seçiniz"))
        sayi2=int(input("2. Sayiyi seçiniz"))
        print("Sonuç",sayi1+sayi2)

    elif islem==2:
        sayi1=int(input("1. Sayiyi seçiniz"))
        sayi2=int(input("2. Sayiyi seçiniz"))
        print("Sonuç",sayi1-sayi2)

    elif islem==3:
        sayi1=int(input("1. Sayiyi seçiniz"))
        sayi2=int(input("2. Sayiyi seçiniz"))
        print("Sonuç",sayi1*sayi2)

    elif islem==4:
        sayi1=int(input("1. Sayiyi seçiniz"))
        sayi2=int(input("2. Sayiyi seçiniz"))
        print("Sonuç",sayi1/sayi2)

print("GULE GULE")
        
