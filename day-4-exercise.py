##1.0 VIRTUAL COIN TOSS PROGRAM

import random

result = random.randint(0, 1)

if result == 1:
  print("Heads")
else:
  print("Tails")

##2.0 BANKER ROULETTE - WHO WILL PAY FOR THE MEAL?
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

name_count = len(names)

random_number = random.randint(0, name_count - 1)

random_name = names[random_number]
#0R random_name = random.choice[names]

print(f"{random_name} is going to buy the meal today!")

##3.0 TREASURE MAP
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

x = int(position[0])
y = int(position[1])

selected_row = map[x - 1]
selected_row[y - 1] = "X"

#or map[x - 1][y - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

