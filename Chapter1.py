import random

def main():
    print("Chapter One")

main()

def introduction():
    print("It's cold at night, wolves are howling, and almost time for bed")
    print("Player is lurking through the woods to find shelter, not knowing something may be watching.")
    print("Player is walking further into the woods to find a shelter")
    print("Player looks around, terrified and alone!")
    print("Player stumble a path. Left is further into darker territory, right is a path heading to shelter.")
    print()

def LetsChoose():
    choose = ""
    while choose != "Left" and choose != "Right":
        choose = input("You must choose, Now! Which way do you want to go(Left or Right)?: ")

    return choose

introduction()
LetsChoose()

def LetsCheckFirst(LetsChoose):
    print("You headed down the path")
    print("You made it!")

CorrectlyChoosen = random.randint(1, 2)

if LetsChoose == str(CorrectlyChoosen):
    print("You've are headed to the shelter")
    print("You've made it, thus far!")
else:
    print("You can't see nor hear anything! AAAAAAHHH!")
    print("You are starting to sink in quick sand")
    print("You seem to get out the quick sand")
    print("You see a dead animal corspe, crisped and meatless")


introduction()
LetsChoose()
LetsCheckFirst(LetsChoose)

