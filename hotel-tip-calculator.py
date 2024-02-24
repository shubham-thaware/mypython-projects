#Greetings
print("**** ----- Welcome to Hotel Tip Genrator ----- ****")

# Asking for bill amount 
bill_amount = float(input("Please enter the Bill Amount here ------> ₹"))

# Asking for tip 
tip_amount = int(input("Please help us with, how much percentage Tip you want to give? (10, 12 or 15) ----->  "))

#Asking to divide the amount in people 
split = int(input("How many people split the bill ----->   "))


#tip amount converted into percentage
tip_bill = bill_amount * tip_amount / 100

# Adding the bill & tip together
actual_bill = bill_amount + tip_bill


#Actuall bill with tip 
final_bill_amount = round(actual_bill / split, 2)

#printing final amount with per person 
print(f"Your Final Bill including the TIp Per-Person is ----> ₹ {final_bill_amount}")
