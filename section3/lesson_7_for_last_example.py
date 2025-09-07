rakamlar="0123456789"

sayac=0
for a in rakamlar:
    for b in rakamlar:
        for c in rakamlar:
            sayac=sayac+1
            sifre=a+b+c
            print(sifre)


#dongu bitti
print("toplam",sayac,"adim")
