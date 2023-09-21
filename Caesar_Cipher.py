#Encrypting a message using the cipher method. 
text = input("Enter your message: ")#asks the user to enter the unencrypted message
cipher = '' #prepares a string for an encrypted message

for char in text: #starts the iteration through the message
    if not char.isalpha(): #if the current alphabet is not alphabetic ignore it
        continue
    char = char.upper()  #convert the letter to upper-case
    code = ord(char)+1    #get the code of the letter and increment it by one
    if code > ord('Z'):    #if the resulting code has left the latin alphabet(it's greater than the Z code)
        code = ord('A')    #......change it to the A code
    cipher += chr(code)   #append the received character to the end of the encrypted message

print(cipher) #print the cipher




#Test 2
#Decrypting a message
cipher = input("Enter your cryptogram: ")
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char)-1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)





#Test 3
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ((char_code - ord('a') + shift) % 26) + ord('a')
            if is_upper:
                char_code -= 32  # Convert back to uppercase if the original character was uppercase
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char  # Preserve non-alphabet characters

    return encrypted_text

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter a shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Invalid shift value. Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    user_text = input("Enter a line of text to encrypt: ")
    shift_value = get_valid_shift()
    encrypted_text = encrypt(user_text, shift_value)
    print("Encrypted text: ", encrypted_text)

    

    