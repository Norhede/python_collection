class Color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
   
   
def go_again():
    print("\nWould you like to try again?")
    another_go = input("Type " + Color.GREEN + Color.BOLD  + "1 to try again, " + Color.RED + "2 to quit entirely.\n" + Color.END)
    if another_go == "1":
        start_program()
    elif another_go == "2":
        print("\nThat's okay, thanks for trying out the application - have a nice day :-)\n")
        quit()
    else:
        print("\nI'm sorry, I don't know that command.")
        go_again()


def check_all_letters(user_input):
    letter_count = 0
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in user_input:
        if i in "abcdefghijklmnopqrstuvwxyz":
            if i in all_letters:
                all_letters.remove(i)
            letter_count += 1
    if len(all_letters) > 0:
        print("There are " + str(letter_count) + " letters in all! However, you didn't use the following letters at all:")
        print(all_letters)
    else:
        print("There are " + str(letter_count) + " letters in all - and you used them all at least once!")
    go_again()


def check_consonants(user_input):
    letter_count = 0
    all_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    for i in user_input:
        if i in "bcdfghjklmnpqrstvwxz":
            if i in all_consonants:
                all_consonants.remove(i)
            letter_count += 1
    if len(all_consonants) > 0:
        print("There are " + str(letter_count) + " consonants in all! However, you didn't use the following consonants at all:")
        print(all_consonants)
    else:
        print("There are " + str(letter_count) + " consonants in all - and you used them all at least once!")
    go_again()


def check_vowels(user_input):
    letter_count = 0
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in user_input:
        if i in "aeiouy":
            if i in all_vowels:
                all_vowels.remove(i)
            letter_count += 1
    if len(all_vowels) > 0:
        print("There are " + str(letter_count) + " vowels in all! However, you didn't use the following vowels at all:")
        print(all_vowels)
    else:
        print("There are " + str(letter_count) + " vowels in all - and you used them all at least once!")
    go_again()


def start_program():
    user_input = input(Color.BOLD + Color.UNDERLINE + "\nType in your input!\n" + Color.END) + ""
    user_input = user_input.lower()
    print("\nYou have 3 options: ")
    input_command = input(Color.GREEN + Color.BOLD + "1 for total letters, " + Color.BLUE + "2 for consonants, " + Color.YELLOW + "3 for vowels.\n" + Color.END)
    if input_command == "1":
        check_all_letters(user_input)
    elif input_command == "2":
        check_consonants(user_input)
    elif input_command == "3":
        check_vowels(user_input)
    else:
        print("\nI'm sorry, I don't know that command. Please start over.")
        start_program()


def main():
    start_program()

main()
