#PredefinedCost
preCost = int(input("Enter your Budget: "))

print("Estimated cost for the following expenses.")
venue = int(input("Venue: "))
catering = int(input("Catering: "))
decors = int(input("Decorations: "))
enter = int(input("Entertainment: "))
misc = int(input("Miscellaneous: "))

#compute all expenses
total_expenses = venue + catering + decors + enter + misc
leftOverMoney = preCost - total_expenses
print(f"The total expenses are {total_expenses}")

#compare budget to cost
if preCost < total_expenses:
    print("You are on a low budget!")
else:
    print(f"You're good, you have {leftOverMoney} left in the budget!")
