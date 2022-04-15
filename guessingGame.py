import random
print("Number Guessing Game")
number=random.randint(1,9)
chance=0
print("Guess a number between 1 and 9 : ")

while chance<5:
    if guess==number:
        print("You Won! :)")
        break
    
    elif guess<number:
        print("Too Low :(")
    
    else:
        print("Too High :(")

    chance+=1

if not chance<5:
 print("You Lost! Thenumber is",number) 
 