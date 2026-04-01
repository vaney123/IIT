#1. Semester grade
# Write a program that requests the numeric grades on a midterm and a final exam

import math

def semesterGrade(midterm, final):
    average = (midterm + 2 * final) /3
    avg = ceil(average)

    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg <= 89:
        return 'B'
    elif 70 <= avg <= 79:
        return 'C'
    elif 60 <= avg <= 69:
        return 'D'
    else:
        return 'F'
    
def ceil(number):
    return math.ceil(number)

def main():
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final exam grade: "))

    grade = semesterGrade(midterm, final)
    print(f"Semester Grade: {grade}")

main()

#2. Planets
# Write a program that displays the names of the planets (see list below) in the list Planets in descending order by surface area.

def main():
    planets = [
        ('Mercury', 75, 1),
        ('Venus', 460, 2),
        ('Mars', 140, 4),
        ('Earth', 510, 3),
        ('Jupiter', 62000, 5),
        ('Neptune', 7640, 8),
        ('Saturn', 42700, 6),
        ('Uranus', 8100, 7)
    ]

    sort_planets = sorted(planets, key = lambda x: x[1], reverse=True)

    print("Sorted by surface area in descended order:")

    for planet in sort_planets:
        print(planet[0], end=" ")

main()
