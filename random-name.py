import random
names= ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
#names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
count_name = len(names)
names_list=random.randint(0, count_name -1)
who_pays = names[names_list]
print(who_pays +" is going to buy the meal today!")