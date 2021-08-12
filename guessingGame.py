import random
chances = 0
lowbond = int(input("What is the minimum value to guess? "))
upbond = int(input("What is the maximum value to guess? "))
ranum = int(random.randint(lowbond, upbond))
print("Number Guessing Game!!")
print("Guess a number between", lowbond, "and", upbond, "...")
while chances < 5:
    
    guess = int(input("Enter your guess: "))

    if guess == ranum:
        print("Congratulations, YOU WON!!")
        break
    elif guess < ranum:
        chances += 1
        print("Your guess was too low; Guess a number higher than", guess, "...")
    elif guess > ranum:
        chances += 1
        print("Your guess was too high; Guess a number lower than", guess, "...")
    else:
        print("Invalid input; Please enter an integer...")

    if not chances < 5: 
        print("YOU LOST!! The number was", ranum, "...")
        print("Better luck next time...")