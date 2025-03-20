#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pass_pick = ''

# def pick_char(char_list, num_chars):
#     global pass_pick
#     for num in range(0, num_chars):
#         random_num = random.randint(0, len(char_list) - 1)
#         pass_pick += char_list[random_num]

# pick_char(letters, nr_letters)
# pick_char(symbols, nr_symbols)
# pick_char(numbers, nr_numbers)

# print(pass_pick)

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_pick = ''

sum_chars = nr_letters + nr_symbols + nr_numbers
for num in range(sum_chars):
    random_num = random.randint(0, 2)
    if random_num == 0:
        letter_num = random.randint(0, len(letters) - 1)
        password_pick += letters[letter_num]
        sum_chars -= 1
        
    elif random_num == 1:
        symbol_num = random.randint(0, len(symbols) - 1)
        password_pick += symbols[symbol_num]
        sum_chars -= 1
    else:
        number_num = random.randint(0, len(numbers) - 1)
        password_pick += numbers[number_num]
        sum_chars -= 1
        
print(password_pick)
        