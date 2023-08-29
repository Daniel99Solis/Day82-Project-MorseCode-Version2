# ------------------------ Morse Code ---------------------------------------- #
# I notice that the downside of using an API is that many o them have restrictions on how many
# request we can do by day. So I am going to add the symbols and translations of the Morse Code
# and having this code to do all the functionality without requesting anything

from const import header, list_english, list_morse_code

# Variables to use in the program
continue_translating = True
list_english_to_morse = []
list_morse_to_english = []
successful_translation = True
print(header)

# Loop to repeat the funtion of the program
while continue_translating:
    print("This program translater Morse Code, Type the option you want to execute: ")
    print("1. From English to Morse Code")
    print("2. From Morse Code to English")
    choice = input("Your choice: ")
    valid_choice = choice == "1" or choice == "2"
    while not valid_choice:
        print("Sorry, that is not a valid option, Select one of the next: ")
        print("1. From English to Morse Code")
        print("2. From Morse Code to English")
        choice = input("Your choice: ")
        valid_choice = choice == "1" or choice == "2"

# Option 1 to translate from English to Morse Code
    if choice == "1":
        user_text = input("Please enter the English Text to translate into Morse Code: ").lower()
        list_user_text = list(user_text)
        for letter in list_user_text:
            if letter in list_english:
                index = list_english.index(letter)
                list_english_to_morse.append(list_morse_code[index])
                list_english_to_morse.append(" ")
                successful_translation = True
            else:
                successful_translation = False
        if successful_translation:
            translation = ''.join(list_english_to_morse)
            print("The translation for the text from English to Morse Code you enter is the next: ")
            print(translation)
        else:
            print("Sorry we couldn't translate your text to Morse Code, the valid characters are: ")
            print(list_english)

# Option 2 to translate from Morse code to English
    else:
        morse_code = input("Please enter the Morse Code to translate into English: ")
        list_morse_user = morse_code.split()
        print(list_morse_user)
        for code in list_morse_user:
            if code in list_morse_code:
                index = list_morse_code.index(code)
                list_morse_to_english.append(list_english[index])
                successful_translation = True
            else:
                successful_translation = False
        if successful_translation:
            translation = ''.join(list_morse_to_english)
            print("The translation for the text from Morse Code to English you enter is the next: ")
            print(translation)
        else:
            print("Sorry we couldn't translate your Morse Code to English, the valid characters are: ")
            print(list_morse_code)

# Ask the user if they want to repeat the program
    want_continue = input("Do you want to translate again Y/N: ").lower()
    valid_answer = want_continue == "y" or want_continue == "n"
    while not valid_answer:
        print("Sorry that is not a valid option")
        want_continue = input("Do you want to translate again Y/N: ").lower()
        valid_answer = want_continue == "y" or want_continue == "n"
    if want_continue == "n":
        continue_translating = False
    list_english_to_morse = []
    list_morse_to_english = []

print("Thank you for using the program 🤗")