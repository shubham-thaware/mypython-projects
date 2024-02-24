#This program is based on else if condition with nested if else
height= float(input("Please enter your height in cm ----> ")) 
bill = 0
if height >= 120:

    print("WOW, You can ride rollercoster !!")
    
    age = int(input("Please enter your age -----> "))

    if age < 12:
        bill = 5
        print("Child ticket are $5.00")
        
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.00")
        
    elif age > 18:
        bill = 10
        print("Adult ticket are $10.00")

    wants_photo = input("Do you want to be photo taken, Y & N --> ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
        

else:
    print("OPPS, You need to grow taller!!")