age=int(input("Enter your age"))
student=input("Are you a student? [Y/N]").upper()

if age<=8:
    print("You've got kids discount")
    
elif  age>=10 and student=="Y":
    print("You've got student discount")
    
elif age>22 and student=="N":
    print("You dont have any discount")

elif age>=65:
    print("You've got senior discount")
else:
    print("Sorry, We can't use any discount")

