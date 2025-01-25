import random
while True :
    inputfromuser =str(input("enter rock paper or sissors "))
    possibleact=["rock","paper","sissors"]
    computersactons=random.choice(possibleact)
    print("the computer chose",computersactons)
    if computersactons==inputfromuser:
        print ("it's a tie")
    elif computersactons=="rock" and inputfromuser=="paper" or computersactons=="paper" and inputfromuser=="sissors" or computersactons=="sissors" and inputfromuser("rock"):
        print("you win")
    else:
        print("you lost")