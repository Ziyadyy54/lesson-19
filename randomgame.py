import random
num =int(random.randint(1,10))
lifes=3
print("enter a number to win the game !")
hi=True
while hi:
    guess=int(input("enter your best guess"))
    if guess == num:
        print ("YOU  WIN! well done ")
        print("the number was",num)
        break
    else:
        print ("try again")
        lifes=lifes-1
        print("you have ",lifes,"lifes remaining")
        if lifes==0:
            print("you lost")
            break
