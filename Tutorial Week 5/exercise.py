#1
num = 5
while True:
    num = 2 * num
    if num % 4 == 0:
        break
print(num)

#2
num = 3
while num < 15:
    num += 5
print(num)

#3
oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
    i = i - 1
print(", ".join(oceans))


#4
for i in range(3, 7):
    print(2 * i)

#5
num = 5
for i in range(num, 2 * num - 2):
    print(i)

#6
for countdown in range(10, 0, -1):
    print(countdown)

#7
numEvens = 0
sumOfEvens = 0

list1 = [2, 9, 6, 7, 12]
for num in list1:
    if num % 2 == 0:
        numEvens += 1
        sumOfEvens += num
print(numEvens, sumOfEvens)

#8
numOfNumbers = 0
list1 = ["three", 4, 5.7, "six", "seven", 8, 3.1416]
for item in list1:
    if isinstance(item, str):
        continue
    numOfNumbers += 1
print(numOfNumbers)

#exercise9

for num in range (1,10,2):
    print(num)

#exercise 10
total = 0
count = 0
total_no = int(input("Enter a number:"))

while count < total_no:
    num = int(input("Enter a number:"))
    total+=num
    count+=1
print("Total:", total)

#exercise 11
L = ["sentence", "contains", "five", "words."]
L.insert(0, "This")
print(" ".join(L))

del L[3]
L.insert(3, "six")
L.insert(4, "different")
print(" ".join(L))

#exercise 12
name = input("Enter name with two parts: ")
L = name.split()
print("{0:s}, {1:s}".format(L[1], L[0]))

#exercise 13
nums = [6, 2, 8, 1]
print("Largest Number:", max(nums))
print("Length:", len(nums))
print("Total:", sum(nums))

#exercise 14
tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print(" ".join(tuple2))

#exercise 15
# Four virtues presented by Plato
virtues = ("wisdom", "courage", "temperance", "justice")
print(virtues[4])

#exercise 16
list1 = [1, "two", "three", 4]
print(" ".join(list1))

#exercise 17
## Display the numbers from 1 through 5.
num = 0
while True:
    num = 1
    print(num)
    num += 1

#exercise 18
celsius = 10
print("Celsius/Farenheit")
while celsius <= 30:
    f = (9/5 * celsius) + 32
    print("{0:^6}\t{1:^10.0f}".format(celsius,f))
    celsius += 5

#exercise 19
w = str(input("Enter the phrase:")).lower()
count = 0

for ch in w:
    if ch in "aeiou":
              count +=1
print("Total vowels:", count)

#Case Study
#Starter
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = [] # list of (title, qty, price_each)
subtotal = 0

#partD
def apply_group_discount(qty, price_each):
    total = qty * price_each
    if qty >= 4:
        total *= 0.9
    return total

def apply_member_discount(total, is_member):
    if is_member:
        total *= 0.95
    return total

#TODO: use a while loop that continues until the user enters 'done'
# 1) ask for movie title (case sensitive is fine)

while True:
    title = input("Enter the movie title or done: ").title()

    if title == "Done":
        break

# 2) if title not in movies, print the available keys and continue
    if title not in movies:
        print("Movies not available. The movies available are:\n",", ".join(movies.keys()),"\n")
        continue
        
# 3) ask for quantity (int)
    try:
        qty = int(input("Enter quantity:"))
    except ValueError:
        print("Invalid Quantity! Try Again!")
        continue
            
            # 4) append (title, qty, movies[title])to purchases
    purchases.append((title, qty, movies[title]))

    # 5) optional: track running subtotal
    cost = movies[title] * qty
    subtotal += cost
            
    print(f"Added: {title} x {qty} = ${cost:.2f}\n")
    #print(f"{title} x {qty} = ${subtotal:.2f}\n")

#partB
grand_total = 0

for title, qty, price_each in purchases:
    line_total = apply_group_discount(qty, price_each)
    grand_total += line_total
    print(f"{title} x {qty} = ${line_total:.2f}")

member = input("\nDo you have a member code? (yes/no): ").lower() == "yes"
grand_total = apply_member_discount(grand_total, member)

print(f"\nFinal Total: ${grand_total:.2f}")

#partC
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + (qty * price_each)

for title in tickets_by_movie:
    print(f"{title}: {tickets_by_movie[title]} tickets, ${revenue_by_movie[title]:.2f}")

#partE
#top selling movie
top_title = None
top_qty = -1

for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty

print("\nTop seller:", top_title, "-", top_qty, "tickets")

#sort by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)

print("\nMovies sorted by revenue:")
for title, revenue in sorted_by_rev:
    print(f"{title}: ${revenue:.2f}")

#average tickets per purcharse
total_tickets = sum(qty for _, qty, _ in purchases)
avg_tickets = total_tickets / len(purchases) if purchases else 0

print(f"\nAverage tickets per purchase: {avg_tickets:.2f}")

        
print("\nFinal Purchases:")
for item in purchases:
    print(item)
print(f"Total: ${subtotal:.2f}")


            

