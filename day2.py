#creating functions
"""def display_message(functions):
    print(f"We're learning about {functions.title()}")
display_message("functions")

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")
favorite_book("Alice in Wonderland")

#Arguments and Parameters
#Positional Arguments
def describe_pet(animal_type,animal_name):
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()} is called {animal_name.title()}")
describe_pet('dog','jellie')
#keyword argument
def describe_pet(animal_type,animal_name):
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()} is called {animal_name.title()}")
describe_pet(animal_name='jelly',animal_type='dog')

def make_shirt(shirt_size,shirt_text):
    print(f"The shirt size is: {shirt_size} \nThe shirt message is: {shirt_text}")
make_shirt("Medium","You look cool")

def make_shirt(shirt_size="large",shirt_text="I love python"):
    print(f"The size of the shirt is {shirt_size} \nThe message is {shirt_text}")
make_shirt()
make_shirt(shirt_size="Medium")
make_shirt(shirt_size="Small",shirt_text="I hate youuu(●'◡'●)")

def describe_city(city_name,country="Iceland"):
    print(f"{city_name.title()} is a city in {country.title()}")
describe_city(city_name="Reykjavik")
describe_city(country="kenya",city_name="nairobi")

#Return Values
def get_formatted(first_name,last_name):
    full_name=f"{first_name.title()} {last_name.title()}"
    return full_name
musician=get_formatted('jimi','hendrix')
print(musician)

#Making an argument optional
def get_formatted(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f"{first_name.title()} {middle_name.title()} {last_name.title()} "
    else:
        full_name=f"{first_name.title()} {last_name.title()}"
    return full_name
musician=get_formatted(first_name='Bien',last_name='Baraza')
print(musician)

#Return a dictioanary
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=None):
    person={'first':first_name,'last':last_name}  
    if age:
        person['age'] = age
    return person
musician=build_person('Jimi','Hendrix',age=27)
print(musician)

#using a function with a while loop(infinite loop)
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
while True:
    print("Please enter your name:")
    f_name=input("First name: ")
    l_name=input("Last name: ")
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name}")

#using a function loop without infinite loop
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
while True:
    print("Please enter your name")
    print("Enter 'q' if you want to quit")
    f_name=input("First name: ")
    if f_name=='q':
        break
    l_name=input("Last Name: ")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name}")

def city_country(city_name,city_country):
    print(f"{city_name},{city_country}")
city_country("Santiago","Chile")

def make_album(artist_name,album_title,number_of_songs=None):
    artist={'name':artist_name,
            'album':album_title}
    if number_of_songs is not None:
        artist['songs']=number_of_songs
    return artist
musician_1=make_album("Bien","Barasa",number_of_songs=10)
musician_2=make_album("Avicii","Nights")
musician_3=make_album("Kinoti","Greeen Room",number_of_songs=5)
print(musician_1)
print(musician_2)
print(musician_3)

def make_album(artist_name,album_title,songs=None):
    artist={'name':artist_name,
            'album':album_title,
            }
    if songs is not None:
        artist['song']=songs
    return artist
while True:
    print("\nEnter the artist name")
    print("(Enter 'q' if you want to quit)")
    name_artist=input("Enter the name of the artist: ")
    if name_artist=='q':
        break
    album_name=input("Enter name of the album: ")
    if album_name=='q':
        break
    songs_number=input("Enter the number of songs: ")
    if songs_number=='q':
        break
    musician_discography=make_album(name_artist,album_name,songs_number)
    print(f"The artist's discography is {musician_discography}")

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_designs=unprinted_designs.pop()
        print(f"Printing models: {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['phones','pendants','watch']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


def show_messages(messages):
    for text in messages:
        print(text)

messages=['\nHeyy how are you'
          '\nHow are you doing'
          '\nIts been so long']
show_messages(messages)"""


def show_messages(messages,sent_messages):
    while messages:
        current_messages=messages.pop()
        print(f"The following are the current messages: {current_messages}")
        sent_messages.append(current_messages)

def send_messages(sent_messages):
    
    print("\nThe following are the sent messages: ")
    for text in sent_messages:
        print(text)

messages=['\nHeyy how are you'
          '\nHow are you doing'
          '\nIts been so long']
sent_messages=[]

show_messages(messages,sent_messages)
send_messages(sent_messages)


