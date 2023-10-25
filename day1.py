#027
number = float(input("Enter a number with lots of decimals:"))
number = number*number
print(round(number,2))
import math
numb = int(input("Enter a number greater than 500:"))
numb = math.sqrt(numb)
print(round(numb,2))

import math
print(round(math.pi,5))

import math
radius = float(input("Enter a radius:"))
print(math.pi*radius**2)

import math
radius = float(input("Enter radius:"))
height = float(input("Enter height:"))
volume = 2*math.pi*radius**2*height
print(round(volume,3))

#accessing an element from a list
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

message = f"I love{bicycles [0]}"
print(message)

#Modifying elements in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements in a list using append
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
motorcycles.append('audi')
print(motorcycles)

#inserting elements to a list
motorcycles=['honda','yamaha','suzuki']
#you can add an element to your list at any position by specifying the index of the new element
motorcycles.insert(0,'ducati')
print(motorcycles)

#removing an item using del statement
motorcycles=['honda','yamaha','suzuki']
# use del to remove an item from a list using the position index
del motorcycles[0]
print(motorcycles)

motorcycles=['honda','audi','yamaha','honda']
del motorcycles[2]
print(motorcycles)

#removing an item using pop() method
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
#pop removes the last item in a list but it can still be accessed
popped_motorcycles=motorcycles.pop()
print(popped_motorcycles)


#popping items from any position in a list
#One can use pop to remove an item from any position in a list by including the index of the item you want tot remove in parenthesis
motorcycles=['honda','suzuki','audi','bmw']
first_owned=motorcycles.pop(0)
print(f"I love {first_owned.title()}")

#removing an item by value using remove() method
motorcycles=['honda','yamaha','suzuki']
motorcycles.remove('suzuki')
print(motorcycles)

#sorting a list permanently using sort() method
cars=['bmw','audi','isuzu','mahindra']
cars.sort()
print(cars)
#Sorting a list in reverse alphabetical order by passing the argument reverse=True
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with the sorted() function
cars=['bmw','audi','isuzu','mahindra']
print("here is the original list:")
print(cars)
# sorted function does not affect the original list
print("\nHere is the sorted list:")
print(sorted(cars))

#printing a list in reverse order using the reverse() method
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

#finding the length of a string
cars=['bmw','audi','toyota','subaru']
len(cars)

#Exercise
travel_destinations=['Jamaica','Barbados','Chile','Canada','Hungary']
print(travel_destinations)

print(sorted(travel_destinations))

travel_destinations.sort(reverse=True)
print(travel_destinations)

travel_destinations.reverse()
print(travel_destinations)

travel_destinations.sort()
print(travel_destinations)

#looping through lists
cars=['audi','bmw','toyota','mazda']
for cars in cars:
    print(cars)


cars=['audi','bmw','toyota','mazda']
for cars in cars:
    print(f"{cars}, is a good car")
    print(f"I want to own a {cars} \n")
print("I'd love to drive them")

#using range() function-makes it easy to generate a series of numbers
for value in range(1,5):
    print(value)
#using range to make a list of numbers
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
    print(squares)

#slicing a list-you specify the index of the first and last element you want to work with.
players=['charles','roberto','sane','mane','kane']
print(players[0:3])
print(players[2:])#starts the list from index 2
print(players[:4])

#looping through a slice
players=['charles','roberto','sane','mane','kane']
print("Here are the first three players:")
for players in players[:3]:
    print(players.title())

#copying a list
my_cars=['bmw','audi','toyota','isuzu']
your_cars=my_cars[:]
my_cars.append('Mercedes')
your_cars.append('bugatti')
print(f"I love:")
print(my_cars)

print("\n You love:")
print(your_cars)

my_fruits=['mango','apples','pineapples']
my_fruits.append('oranges')
print("I love:")
for my_fruits in my_fruits:
    print(my_fruits)

friends_fruits=['oranges','mango','pineapples']
friends_fruits.append('apples')
print("\nMy friend loves:")
for friends_fruits in friends_fruits:
    print(friends_fruits)


#TUPLES
dimensions=(200,50)
print(dimensions[0])
#looping through all values in a tuple
for dimensions in dimensions:
    print(dimensions)

#writing over a tuple
dimensions=(200,50)
print("Original dimensions:")
for dimensions in dimensions:
    print(dimensions)


dimensions=(400,100)
print("\nModified dimensions:")
for dimensions in dimensions:
    print(dimensions)


#DICTIONARIES-collection of key-value pairs
alien={'color':'green','points':5}
print(alien['color'])
print(alien['points'])

#accessing values in a dictionary
alien_o={'color':'green','points':5}
new_points=alien_o['points']
print(f"You just earned {new_points} points!")

#adding new key-value pairs
alien_o={'color':'green','points':5}
alien_o['x_position']=0
alien_o['y_position']=25
print(alien_o)

#starting with an empty dictionary
alien_o={}
alien_o['color']='green'
alien_o['points']=5
print(alien_o)

#modifying values in a dictionary
alien_o={'color':'green'}
print(f"\nThe alien is {alien_o['color']}")

alien_o['color']='yellow'
print(f"The alien is now {alien_o['color']}")
#A dictionary of similar objects
favorite_language={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'phil':'python'
}
language=favorite_language['Sarah'].title()
print(f"Sarah's favorite language is {language}")

#Using get() to access values.The get method requires a key as a first argument
alien_0={'color':'green','speed':'slow'}
point_value=alien_0.get('points','No point value assigned')
print(point_value)

# looping through a dictionary
user_o={
    'Username':'Ofemi',
    'First':'Enrico',
    'Last':'Fermi'
}
for key,value in user_o.items():#includes name of the dictionary followed by the method items which returns a key value pairs.
    print(f"\nKey:{key}")
    print(f"Value:{value}")


favorite_languge={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'phil':'python'
}
for name,language in favorite_languge.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

#looping through keys
favorite_languge={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'phil':'python'
}
for name in favorite_languge.keys():
    print(f"{name.title()}")

#deleting entries from a key
favorite_languge={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'Phil':'python'
}
removed_value=favorite_languge.pop('Sarah')
print(favorite_languge)

#looping through dictionary's keys in a particular order
favorite_languge={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'Phil':'python'
}
for name in sorted(favorite_languge.keys()):
    print(f"{name.title()}, Thank you for participating")


#looping through all values in a dictionary
favorite_languge={
    'Jen':'Python',
    'Sarah':'c',
    'Edward':'ruby',
    'Phil':'python'
}
print("The following languages have been mentioned:")
for language in favorite_languge.values():
    print(language.title())

rental_car=input("which car do you want? ")
print(f"Let me see if I can find you a {rental_car.title()}")
 
restaurant_booking=input("How many people are in the dinner group? ")
restaurant_booking=int(restaurant_booking)
if restaurant_booking > 8:
    print("They'll have to wait")
else:
    print("Their table is ready")

multiples_of_ten=input("Enter a number: ")
multiples_of_ten=int(multiples_of_ten)
if multiples_of_ten % 10 == 0:
    print(f"The number {multiples_of_ten} is a multiple of ten")
else:
    print(f"The number {multiples_of_ten} is not a multiple of ten")

prompt="tell us your first name for a personalized message: "
prompt += "\n What's your first name: "
name=""
while name != 'quit':
    name=input(prompt)
    print(name)

prompt="\nPlease enter the name of a city you have visited: "
prompt+="\n(Enter 'quit' when you're finished)."
while True:
    city=input(prompt)
    if city=="quit":
        break
    else:
        print(f"I'd love to go to {city.title()}")

while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"The cost of your movie ticket is ${ticket_price})

toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == 'quit':
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("Your pizza with the following toppings is ready:")
for topping in toppings:
    print("- " + topping)

#moving items from one list to another
unconfirmed_users=['Alice','Brian','Ken']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)
#display all confirmed users
print("\nThe following users have beeen confirmed: ")
for confirmed_users in confirmed_users:
    print(confirmed_users)





