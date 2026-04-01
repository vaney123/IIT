#1. Cost of postage
#The original postage cost of airmail letters was 5 cents for the first ounce and
#10 cents for each additional ounce.
#Write a program to compute the cost of a letter whose weight is given by the user.
#The cost should be calculated by a function named cost.
#The function cost should call a function named ceil that rounds non-integer numbers up to the next integer.

def cost(ounces):
    return 0.05 + (0.10 * ceil(ounces-1))

def ceil(ounces):
    if int(ounces) != ounces:
        return int(ounces + 1)
    else:
        return ounces

def getInput():
    'Get the weight of postage from user'
    return float(input("Enter number of ounces: "))

def displayOutput(cost):
    print("Cost: ${0:.2f}".format(cost))
    
def main():
    #input --> Process --> Output
    ounces = getInput()
    postageCost = cost(ounces)
    displayOutput(postageCost)

main()

#2. Credit card payment
#Write a program to calculate the balance and minimum payment for a credit card statement.

RATE = 0.015
def calculate(oldBalance, charges, credit):
    newBalance = (oldBalance*RATE) + charges - credit + oldBalance
    if newBalance <= 20:
        minPayment = newBalance
    else:
        minPayment = 20 + 0.10 * (newBalance-20)
    return newBalance, minPayment

def getInput():
    'Get the old balance and charges'
    oldBalance = float(input("Enter old balance: "))
    charges = float(input("Enter charges: "))
    credit = float(input("Enter credit: "))
    return oldBalance, charges, credit

def displayOutput(newBalance, minPayment):
    print("New Balance: ${0:.2f}\nMinimum Payment: ${1:.2f}".format(newBalance, minPayment))
    
def main():
    #input --> Process --> Output
    oldBalance, charges, credit = getInput()
    newBalance, minPayment = calculate(oldBalance, charges, credit)
    displayOutput(newBalance, minPayment)

main()

#3. Mortgage calculations
#Write a program to calculate three monthly values associated with a mortgage

def calculate(annualrate, monthlypayment, initialBalance):
    monthlyrate = annualrate / 100 / 12
    
    interestpaid = monthlyrate * initialBalance
    principalreduction = monthlypayment - interestpaid
    endBalance = initialBalance - principalreduction
    return interestpaid, principalreduction, endBalance

def getInput():
    annualrate = float (input("Enter annual rate of interest: "))
    monthlypayment = float(input("Enter monthly payment: "))
    initialBalance = float(input("Enter initial balance: "))
    return annualrate, monthlypayment, initialBalance
    
def displayOutput(interestpaid, principalreduction, endBalance):
    print(f"Interest paid for the month: ${interestpaid:.2f}\nReduction of principal: ${principalreduction:.2f}\nEnd of month balance: ${endBalance:.2f}")

def main():
    annualrate, monthlypayment, initialBalance = getInput()
    interestpaid, principalreduction, endBalance = calculate(annualrate, monthlypayment, initialBalance)
    displayOutput(interestpaid, principalreduction, endBalance)

main()


#4. Wilson’s Theorem
#Write a program that determines whether a number is prime by using the theorem "The number n is a prime number if and only if n divides (n - 1)! + 1.

def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result
    
def isPrime(n):
    if n <= 1:
        return False

    fact = factorial(n)
    return (fact + 1) % n == 0
    
def main():
    num = int(input("Enter a number: "))

    if isPrime(num):
         print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        
main()
    
