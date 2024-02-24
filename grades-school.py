percentage = float(input("Enter the percentage between 0 to 100 without percentage '%' symbol ----> "))
if percentage > 90:
    print("Its Grade ----> A")
elif percentage > 80 and percentage <= 90:  # corrected syntax
    print("Its Grade ----> B")
elif percentage >= 60 and percentage <= 80:  # corrected syntax
    print("Its Grade ----> B")
elif percentage < 60:
    print("Its Grade -----> D")  # corrected spelling
