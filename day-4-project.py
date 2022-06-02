rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

moves = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You have entered an invalid number. You lose!")
else:
  user_output = moves[user_choice]
  print(user_output)
  
  print("Computer chose:")
  
  import random
  
  cpu_choice = random.randint(0, 2)
  cpu_output = moves[cpu_choice]
  
  print(cpu_output)
  
  if user_output == rock:
    if cpu_output == rock:
      print("It's a draw.")
    elif cpu_output == paper:
      print("You lose!")
    else:
      print("You win.")
  elif user_output == paper:
    if cpu_output == rock:
      print("You win!")
    if cpu_output == paper:
      print("It's a draw.")
    else:
      print("You lose.")
  elif user_output == scissors:
    if cpu_output == rock:
      print("You lose.")
    if cpu_output == paper:
      print("You win!")
    else:
      print("It's a draw.")