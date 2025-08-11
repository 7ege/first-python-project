gender=input("Enter your gender [M/F]:").upper()
age=int(input("Enter your age:"))

if gender == "F":
    print("Mandatory military service does not apply to female")
elif gender=="M" and age<20:
    print("You have not reached military age yet")
elif gender=="M" and age>=20:
    print("Time to serve your country...")
else:
    print("I think there is an error in your information")
