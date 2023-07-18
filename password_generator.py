import string
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for _ in range(nr_letters):
    password_list.append(random.choice(string.ascii_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(string.punctuation))

for _ in range(nr_numbers):
    password_list.append(random.choice(string.digits))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is: {password}")