#şifre en az 8 karakter, en az 1 buyuk harf, en az 1 kucuk harf,en az 1 sayi

sifre=input("Şifre giriniz:")
kucukHarf="abcdefghıjklmnopqrstuvwxyz"
buyukHarf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="012345678"

ksayi=0
bsayi=0
dsayi=0

for harf in sifre:
    if harf in buyukHarf:
        bsayi=bsayi+1

    if harf in kucukHarf:
        ksayi=ksayi+1

    if harf in digit:
        dsayi=dsayi+1

if (bsayi==0) or (ksayi==0) or (dsayi==0) or (len(sifre)<8):
    print("Guvensiz sifre")

else:
    print("GÜVENLİ ŞİFRE")
        
