# ------------------------------------------------------
#        Name: Paw Poe
#       Peers: N/As
#  References: Homework 4 Assignment Instructions
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ This def will read the input of the user and see if the secret word, "food" is used.
        If the input does not contain the secret word, "Try Again" will be printed."""
    
    while True:
        text = input("Give me a sentence: ")
        
        if secret_word in text:
            print("You used the secret word!")
            break
        elif "dog" in text or "Dog" in text:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")


# Task 2
def check_greater():
    """ Get two integers from the user and compare them.
        Prints which integer is greater, if equal "try again" will be printed."""
    
    first = int(input("Give me a first integer: "))
    second = int(input("Give me a second integer: "))
    
    while True:
    
        if first == second:
            print("Try again")
            first = int(input("Give me a first integer: "))
            second = int(input("Give me a second integer: "))
        elif first > second:
            print("First is Greater")
            break
        else:
            print("Second is Greater")
            break


# Task 3
def get_special_numbers():
    """ Prints odd number from 1 to 40 that are multiples of 3
        and not multiples of 5."""
    
    for number in range(1,41):
        
        if number % 2 == 0:
            continue
        if number % 3 != 0:
            continue
        if number % 5 == 0:
            continue
        
        print(number)


# Task 4.a
def my_for_loop():
    """ The function has to ask for a string from the user.
        If the word is of a valid length and has no spaces,
        then the function will identify whether each letter is a vowel or consonant."""
    
    word = input("Give me a string: ")
    letters = len(word)
    vowels = ("a", "e", "i", "o", "u", "y")
    
    if 2 > letters or letters > 5 or " " in word:
        print("bad word")
        return
    
    for let in word:
        if let in vowels:
            print("letter", let, " is a vowel")
        else:
            print("letter", let, " is a consonant")

# Task 4.b
def my_while_loop():
    """ Offers the user three choices, option "a" repeats the menu,
        "b" prints "Goodbye" and returns,
        and "c" exits the program, if any other, "try again" prints."""
    
    choose = input("Choose one option: a, b, or c: ")
    
    while choose != "a" and choose != "b" and choose != "c":
        print("try again")
        choose = input("Choose one option: a, b, or c: ")
    
    while choose == "a":
        choose = input("Choose one option: a, b, or c: ")
    while choose == "b":
        print("Goodbye")
        return
    while choose == "c":
        exit()
# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
