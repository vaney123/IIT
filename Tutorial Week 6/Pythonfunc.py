#1 Write fahrenheit_to_celsius(f) that returns °C
def fahrenheit_to_celsius(f):
    'converts'
    return (f - 32) * 5/9

def getInput():
    'gets fahrenheit'
    return float(input("Enter temperature in fahrenheit: "))

def displayOutput(f, c):
    print("${0:.2f} Fahrenheit = {1:.2f} celsius".format(f, c))

def main():
    f = getInput()
    c = fahrenheit_to_celsius(f)
    displayOutput(f, c)

main()


#2 Write is_even(n) that returns True if n is even
def is_even(n):
    return n % 2 == 0

def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print("Even")
    else:
        print("Odd")

main()

#3 Write triangle_area(b, h=1) with default height 1
def triangle_area(b, h=1):
    return 0.5 * b * h

def main():
    base = float(input("Enter base: "))

    area = triangle_area(base)
    print(f"Area of triangle: {area}")

main()
