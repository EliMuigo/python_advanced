#027
"""number = float(input("Enter a number with lots of decimals:"))
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
print(alien['points'])"""

#accessing values in a dictionary
alien_o={'color':'green','points':5}
new_points=alien_o['points']
print(f"You just earned {new_points} points!")

#adding new key-value pairs









