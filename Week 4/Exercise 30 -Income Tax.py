income = float(input("Enter your taxable income: "))

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = income * 0.10
else:
    tax = income * 0.15

print("Your income tax is:", tax)
