import random

# Stone Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose stone
    elif comp == 'stone':
        if you=='scissor':
            return False
        elif you=='paper':
            return True
    
    # Check for all possibilities when computer chose paper
    elif comp == 'paper':
        if you=='stone':
            return False
        elif you=='scissor':
            return True
    
    # Check for all possibilities when computer chose scissor
    elif comp == 'scissor':
        if you=='paper':
            return False
        elif you=='stone':
            return True

print("Comp Turn(Choose Number):\n 1)stone\n 2)paper\n 3)scissor\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

print("comp: Choosed\n")

you = int(input("Your Turn(Choose Number):\n 1)stone\n 2)paper\n 3)scissor\n"))

if you == 1 or you == 2 or you == 3:
    if you == 1:
        you = 'stone'

    elif you == 2:
        you = 'paper'

    elif you == 3:
        you = 'scissor'
else:
    print("Enter Valid Input and Try Again!")   
    exit()

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("It's a tie!")
elif a:
    print("Hurray!, You Won!")
else:
    print("Opps!, You Lose!")