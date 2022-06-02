##Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

py_letters = ""
for random_letters in range(1, nr_letters + 1):
  random_letters = random.choice(letters)
  py_letters += random_letters
  #or py_letters += random.choice(letters)

  
py_symbols = ""
for random_symbols in range(1, nr_symbols + 1):
  random_symbols = random.choice(symbols)
  py_symbols += random_symbols
  

py_numbers = ""
for random_numbers in range(1, nr_numbers + 1):
  random_numbers = random.choice(numbers)
  py_numbers += random_numbers

py_final = py_letters + py_symbols + py_numbers

print(f"Here is your password: {py_final}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for char in range(1, nr_letters + 1):
  password += random.choice(letters)
  #or password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
  
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

random.shuffle(password)

final_password = ""
for char in password:
  final_password += char

print(f"Your password is: {final_password}")