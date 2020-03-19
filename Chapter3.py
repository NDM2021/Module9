inventory = []

def main():
    print("Chapter Three")

main()

def Hello():
    print("The sun sunsets, and the moon is at its peak. Owls are sounding.")
    print("The creature is awakened and ready to feed")
    print("Player must talk to officers and craft weapons for a showdown.")
    print("You decide where you want to go, Speak to officer(Y) or go alone(T)")
    print()

def requit():
    Qualify = ""
    while Qualify != "T" and Qualify != "Y":
        Qualify = input("Make your Choice(Y or T)?:")

    return Qualify

Hello()
requit()


def CheckSurmised(Hello):
    print("You decided to talk to the officers")
    print("They'll help you")



if requit == str(CheckSurmised):
    print("You decided to go alone.")
else:
    print("You don't get any help at all!")
    print("Why you take so long")
    print("Gear up and fight by yourself!")

def interact():
    print("You are walking around in the woods")
    print("You hear a growl")
    print("You continue walking")
    print("Something is watching you in the bushes. Wait! it disappeared in thin air")
    print("You stumbled across a spear made from wood and a sword wrapped in leaves")
    print("Do you want to collect both? Yes or No?")

def choicesMaking():
    Making = ""
    while Making != "Yes" and Making != "No":
        Making = input("Do you want both weapons(Yes or No)?:")

        return Making

def AcquiredItems():
    global inventory
    print("You acquired a Sword and Spear")
    AcquiredItems == input
    if AcquiredItems == "Yes":
        AcquiredItems("Sword and a Spear")

def gotten(item):
    inventory. append(item)



Hello()
requit()
CheckSurmised(Hello)
interact()
choicesMaking()
AcquiredItems()

