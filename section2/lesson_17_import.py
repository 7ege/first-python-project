import datetime
#Imported the date and time module
#The import statement is used in Python to bring in an external module (library).

now=datetime.datetime.now()

hour=now.hour  #13.45 ---> 13

print("Hour:", hour)

if hour >= 7 and hour <= 10:
    print("Good morning")
elif hour >= 11 and hour <= 16:
    print("Good afternoon")
elif hour >= 17 and hour <= 21:
    print("Good evening")
else:
    print("Good night")




    
