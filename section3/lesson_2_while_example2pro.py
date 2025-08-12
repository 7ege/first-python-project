import random                #use random
sayi=random.randint(1,100) #(turkish)1 ile 100 arasında rastgele sayı uret
sayac=0                      #kac kere tahmin ettigimi tutar
tahminim=0

while tahminim!=sayi:
    tahminim=int(input("Tahmin ediniz [1-100]"))
    sayac=sayac+1          #her tahminde sayac 1 artsın
    
    if tahminim<=sayi:
        print("YUKARI")
    if tahminim>=sayi:
        print("AŞAĞI")

#döngü bitti,kaç kere bildigimi yaz
print("BRAVO",sayac,"kerede bildiniz")
        
