def is_palindrome(text):
    #remove the spaces and convert text to lowercase
    clean_text=''.join(text.split()).lower()

    #check if the clean text is equal to reverse
    return clean_text==clean_text[::-1]

if __name__ == "__main__":
    user_text=input("Enter some text: ")

    if not user_text:
        print("Empty text is not a palindrome.")
    elif is_palindrome(user_text):
        print("The entered text is a palindrome.")
    else:
        print("The entered text is not a palindrome.")


