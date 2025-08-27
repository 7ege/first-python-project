turkcekarakterler="üÜğĞiİşŞçÇöÖ"

isim=input("Metin giriniz")

for harf in isim:
    if harf in turkcekarakterler:
        print("Turkce karakter:",harf)
