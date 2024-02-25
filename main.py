import random

def main():

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    random_letters = get_random_letters(nr_letters)
    random_symbols = get_random_symbols(nr_symbols)
    random_numbers = get_random_numbers(nr_numbers)

    combined_characters = random_letters + random_symbols + random_numbers
    random.shuffle(combined_characters)

    generated_password = "".join(combined_characters)

    print(f"Here is your password: {generated_password}")

def get_random_letters(nr_letters):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_length = nr_letters
    random_letters = []
    for i in range(0, list_length):
        random_index = random.randint(0, len(letters) - 1)
        random_letters.append(letters[random_index])
    return random_letters

def get_random_symbols(nr_symbols):
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    list_length = nr_symbols
    random_symbols = []
    for i in range(0, list_length):
        random_index = random.randint(0, len(symbols) - 1)
        random_symbols.append(symbols[random_index])
    return random_symbols

def get_random_numbers(nr_numbers):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_length = nr_numbers
    random_numbers = []
    for i in range(0, list_length):
        random_index = random.randint(0, len(numbers) - 1)
        random_numbers.append(numbers[random_index])
    return random_numbers

main()


