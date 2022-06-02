##1.0 AVERAGE STUDENT HEIGHT

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

sum = 0

for ind_heights in student_heights:
  sum += ind_heights

average_ind = sum / (len(student_heights))

print(round(average_ind))

#or

total_students = 0
for student in student_heights:
  total_students += 1

##2.0 HIGHEST SCORE

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")

## 3.0 SUM OF EVEN NUMBERS

total = 0

for even_numbers in range(2, 101, 2):
  total += even_numbers
print(total)

#or

total2 = 0

for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)

## 4.0 FIZZ BUZZ (Coding Interview Question)

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)