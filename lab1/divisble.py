"Divisibility Check"

number = int(input("Enter a number: "))

if number > 10 and number % 3 == 0 and number % 5 != 0:
    print("Condition met")
else:
    print("Condition not met")
