mailim="egemns@mersin.edu.tr"

at_sayisi=mailim.count("@")
nokta_sayisi=mailim.count(".")
if at_sayisi==1 and nokta_sayisi>=1:
    print("Teknik olarak dogru gorunuyor")

else:
    print("Hatali mail adresi")
