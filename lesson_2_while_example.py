number=17
myGuees=0

while number!=myGuees:
    myGuees=int(input("Please enter the number[1-100]"))

    if myGuees>number:
        print("GO DOWN")
    if myGuees<number:
        print("GO UP")
        

print("Congratulations")
