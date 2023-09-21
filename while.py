pets=['dog','cat','goldfish','cat','dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary with user input
responses={}
polling_active=True

while polling_active:
    name=input("\nWhat is your name: ")
    response=input("Which city do you want to visit")
    