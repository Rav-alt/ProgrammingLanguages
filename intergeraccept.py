userInput = int(input("Enter a number: "))

if userInput == 0:
    print("The number is Zero")
elif userInput > 0:
    print("The number is Positive")
elif userInput < 0:
    print("The number is Negative")
else:
    print("Error")