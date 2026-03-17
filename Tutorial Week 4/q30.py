#30

income = float(input("Enter taxable income: "))

if income <= 20000:
    tax = 0.02 * income
elif income <= 50000:
    tax = 400 + 0.025 * (income - 20000)
else:
    tax = 1150 + 0.035 * (income - 50000)

print("Tax: ", tax)
