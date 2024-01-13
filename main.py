import random, handSign
print("**--**__PYTHON ROCK PAPER SCISSORS GAME__**--**")
print()
choice=int(input("Which Do you want to choose: Rock[0], Paper[1], Scissors[2] "))
arr=[handSign.rock,handSign.paper,handSign.scissors]
temp=random.randint(0,2)
print("YOU CHOSE: \n"+arr[choice])
print("COMPUTER CHOSE: \n"+arr[temp])
if(temp==choice):
    print("IT'S A TIE!!")
elif((temp==0 and choice==1) or (choice==1 and temp==2) or (choice==0 and temp==1)):
    print("YOU LOST!!")
elif((temp==1 and choice==0) or (choice==2 and temp==1) or (choice==1 and temp==0)):
    print("YOU WON!")