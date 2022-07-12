# Geuss game is number guessing game,
# If user number matches with the computer guess number then print correct
import random
N = random.randint(0,50)
while True:
    C =int(input("Enter the number:"))         
    if C<0 or C>50:
        print("Please print between 0-50")
    else:
        if C<N:
            print("Gets higher")
        elif C>N:
            print("get's lower")
        else:
            print("You're correct")
            break
