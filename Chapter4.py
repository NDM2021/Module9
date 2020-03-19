inventory = []

def main():
    print("Chapter Four")

main()

def Tales():
    print("Still night, something lurks in search of food.")
    print("The creatures smells flesh and it hungers for it.")
    print("Player walks around in the woods in search of survivors bu couldn't find any.")
    print("Player have a run in with the creature.")
    print("Player hides behind bushes. Creature is tracking player's scent.")
    print("You watch as the creatures attempts to find you")
    print("you ran back to the shelter")
    print(". Make your choice: Dr are you going to stay in and or go out?")

def Exquisitive():
    Noted = ""
    while Noted != "Stay in" and Noted != "Go out":
        Noted = input("Make haste. Do you want to stay in the shelter? stay in or Go out?:")

        return Noted

Tales()
Exquisitive()

def checkMate(Tales):
    print("You stay in and rest")
    print("The creatures leaves")

if Exquisitive == str(checkMate):
    print("You've left. The creature will eat you for lunch!")
else:
    print("You are the creatures dinner")
    print("The creature manage to appear in the shelter")
    print("Blood splatted over the windows")
    print("Blood spills and runs underneath the door and reached outside")
    print("You died")

Tales()
Exquisitive()
    


