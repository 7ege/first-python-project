n_1=int(input("Enter the number"))
calculating=input("+? -? *? /?")
n_2=int(input("Enter the number"))

if calculating=="+":
    print(n_1+n_2)
elif islemler=="-":
    print(n_1-n_2)
elif islemler=="*":
    print(n_1*n_2)
elif islemler=="/":
    if ikinci==0:
        print("You cant divide 0 ")
    else:
        print(n_1/n_2)
