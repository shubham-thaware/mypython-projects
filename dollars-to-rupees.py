print("_____ Welcome To $Dollars To ₹Rupees Converter_____ ")

#Price of 1$ in Indian Rupees is ₹83.04
one_dollar_in_rupees = float(83.04)   #current rate of 1usd in rupees

print(f"\n   Current Value of ----> $1 = ₹{one_dollar_in_rupees} \n")

#Asking user to enter usd amount to convert in rupees
USD = float(input("\n   Please enter the $USD you want to convert into Rupees ----->  $" ))

#converting the USD into rupees
rupees = float(round(USD * one_dollar_in_rupees, 4))

#printing the final amount in rupees
print(f"Your amount in Rupees is ----> ₹{rupees}")