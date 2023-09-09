import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}',
         '[', ']', '|', ':', '~', '`']

print('welcome to the generative password!!!!!!!')

user_letter = int(input('How many letter would like your password have?:  '))
user_symbols = int(input('how many symbols would you like your password have?:  '))
user_number = int(input('how many numbers would you like password have ?:  '))


password_letter = []
for i in range(1, user_letter+1):
    char = random.choice(letters)
    password_letter += char

for i in range(1, user_symbols+1):
    char = random.choice(symbols)
    password_letter += char

for i in range(1, user_number):
    char = random.choice(numbers)
    password_letter += char

print(password_letter)

random.shuffle(password_letter)
print(password_letter)
password = ''
for char in password_letter:
    password += char
print("Your password is:  {}".format(password))
