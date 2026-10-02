import random

print("Number guessing game!!\n")
print("Start!!!\n")

attempt = 0

secret_num = random.randint(1, 100)

while attempt < 3:
    guessed_no = int(input("enter a number: "))
    attempt += 1

    if guessed_no < secret_num:
        print("You guessed too low wrong.Try again.")
    elif guessed_no > secret_num:
        print("You guessed too high wrong.Try again.")
    else:
        print("Congratulations!!! You guessed the right number.")
        break 