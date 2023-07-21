# this is a tip calculator for friends who are looking to share a bill. 
#it will calculate how much the tip each person should pay taking into account the number of people in the group and output what each person should pay

print("Welcome to the tip calculator.")

# determine what the total bill was and assigne that to a variable
bill = float(input("What was the total bill?  $"))

# determine what the percentage tip the guests would like to give
tip = float(input("What percentage tip would you like to give? e.g 10, 12, 15?  "))

#determine how many people will be splitting the bill
num_people = int(input("How many people to split the bill? "))

final_amount = float((bill/num_people) * (1 + (tip/100)))
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")