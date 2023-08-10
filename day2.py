#Creating a function and calling it
def favorite_book(title):
    print(f"My favorite book is,{title}!")

favorite_book("Alice in borderland")

#Passing Arguments
def make_shirt(shirt_text,shirt_size = "large"):
    print(f"/n The size of the shirt is {shirt_size} and the message is {shirt_text}!")

make_shirt(shirt_text="I love python")

#returning a dictionary
def make_album(name,title,number_of_songs=None):
    album = {'album_name':name,'album_title':title}
    if number_of_songs is not None:
        album['number_of_songs']=number_of_songs
    return album

album_1 = make_album('sam','love')
album_2 = make_album('Adele','Dark',number_of_songs=20)
print(album_1)
print(album_2)

def make_album(album_artist,album_title,number_of_songs=None):
    musician_discography=f"{'album_artist':album_artist,'album_title':album_title}"
    if number_of_songs is not None:
        musician_discography['number_of_songs']=number_of_songs
    return musician_discography
def main():
    print("Enter album information or type quit to exit.")
    while True:
        album_artist = input("Enter the artist's name: ")
        if album_artist.lower()=='quit':
            break

        album_title = input("Enter the name of the album: ")
        if album_title.lower()=='quit':
            break

        number_of_songs = input("Enter the number of albums:")
        if number_of_songs.lower()=='quit':
            break
        
        elif number_of_songs.isdigit():
            number_of_songs = int(number_of_songs)
            musician_discography = make_album(album_artist,album_artist,number_of_songs)
        else:
            musician_discography = make_album(album_artist,album_title)

        print("Album Information")
        print(musician_discography)
if __name__=="__main__":
    main()








    

