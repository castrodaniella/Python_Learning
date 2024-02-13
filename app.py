
"""
weight_lbs = input( 'Weight (lbs): ')
weight_kg = (int (weight_lbs) * 0.453592)

print('Your weight is '+str(weight_kg))

#################################
#Print Lesson
#################################

first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder'
print(message)

course = 'python for b'

print(len(course))
print(course.upper())
print(course.find('P'))

print(course.replace('b', 'Beginners'))

print('python' in course)

print(course.title())

print(course.lower())



#################################
#Arithimetic Lessons
#################################



import math

x = 10 + 3 * 2
print(x)

y = 10 **2
print(y)

z = 100 % 2
print(z)

a = (2 + 3) * 10 - 3
print(a)

b = 2.9
print(round(b))

print(math.floor(2.9))

print(math.ceil(2.9))


#################################
#Conditional Lessons
#################################


is_hot = False
is_cold = True


if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear your jacket")
print("Enjoy your day")


house_price = 1000.000
buyer_good_credit = False
if buyer_good_credit:
    put_down = house_price * 0.1
    print(f"You need to put down 10%. Your down payment is: ${put_down}")
else:
    put_down = house_price * 0.2
    print(f"You need to put down 20%. Your down payment is: ${put_down}")

has_high_income = True
has_high_credit = True
has_not_criminal = False

if has_high_income and not has_not_criminal:
    print("Good buyer")

temperature = 35

if temperature >= 36:
    print("it is hot")
else:
    print("it is cold")

name = "Dani"
if len(name) < 5:
    print("Your name is too short")

i = 1
while i <= 5:
    print('*' * i)
    i += 1

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Try again!")
print("sorry")


#################################
#LOOPS
#################################

for item in 'Python':
    print(item)


for item in range(20):
    print(item)

total = 0
prices = [10, 20, 30]
for item in prices:
    total += item
print(total)

#################################
#LISTS
#################################



large = [10, 4, 1, 8]

largest = 0

for y in large:
    if y > largest:
        largest = y
print(largest)


findDuplicate = [2,3,4,2,6,4,3]


for x in findDuplicate:
    while x in findDuplicate:
        findDuplicate.remove(x)

        
print(findDuplicate)


for x in range (4):
    for y in range(3):
        print(f'({x}, {y})')


        
#################################
#iNTERACTIVE LOOPS
#################################


#numbers = [5,2,5,2,2]
numbers = [1,1,1,1,1,4]
for y in numbers:
    for x in range(y):
        print('x', end="")
    print('')
        




#################################
#Tuples
#################################

customers = (2, 1, 3)

print(customers[0])


#unpacking
x, y, z = customers

print(y)

#################################
#Dictionaries
#################################

customer = {
    "name" : "John Smith",
    "age": 30,
    "is_verified": True

}

print(customer["age"])

print(customer.get("birthday"))

#print(customer["birthday"])

customer["name"] = "Dani"

print(customer["name"])



numbers = input("phone:")
#numberslist = list(numbers)

numberslist = [i for i in numbers]

numbersdict = {
    "1": "one",
    "2": "two",
    "3": "three"
}


for numberlist in numbersdict.keys():
        print(numbersdict[numberlist])




message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊"

}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
"""

#################################
#Functions
#################################

def square(number):
    return number * number

result = square(3)

print(result)

print(square(2))

message = input(">")

def emoji(message):

    words = message.split(' ')
    emojis = {
        ":)" : "😊"

    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)

emoji(message)
