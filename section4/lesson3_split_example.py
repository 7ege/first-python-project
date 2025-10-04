#okulno  D-ISL-001==DOKTORA-ISLETME-1 NUMARALI OGRENCIYIM


okulno=input("Okul numaranizi giriniz ")      #D-ISL-001
okulno=okulno.upper()   #buyuk harfde girse kucuk harfte girse BUYUKHARFE cevirir

bol=okulno.split("-")                         
ogrenimdurumu=bol[0]                  #D         
anabilimdali=bol[1]                   #ISL
yerlesimsirasi=int(bol[2])           #1

cumle=anabilimdali+" alaninda "+ogrenimdurumu+" yapiyorsunuz ve  "+str(yerlesimsirasi)+" inci sira ile girdiniz "
print(cumle)
