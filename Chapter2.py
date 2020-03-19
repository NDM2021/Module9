import random

inventory =[]

def main():
    print("Chapter Two")

main()

def Intro():
    print("The sun starts to rise, and the rooster starts to crow in the morning")
    print("Player grabs bookbag")
    print("Player walks outside and carries on to find food and water")
    print("You come across two berry bushes, 1 is freshly riped, 2 is poisonous")
    print()

def Decide():
        Decide = ""
        while Decide != "2" and Decide != "1":
            Decide = input("Which berry bush would you like?(1 or 2)?:")
    
        return Decide
Intro()
Decide()
def CheckPlease(Decide):
    print("You chose a berry bush")
    print("You collected freshly riped berries")

Correct = random.randint(1, 2)

if Decide == str(Correct):
    print("You collected the berries from a bush")
else:
    print("You consumed poisonous berries")
    print("Your insides begins to degrade")
    print("You die slowly")
    print("You've sucumb to death")
    print("Your body quickly turns to ashes")

def collect():
    global inventory
    print("You've acquired berries")
    if collect == "Yes":
        collect("Berries")
    else:
        print("You decided to leave the berries")
print(inventory)

def insertToInventory(item):
    inventory.append(item)

def MoreItems():
    global inventory
    print("You've gotten water as well")
    MoreItems == input
    if MoreItems == "Yes":
        MoreItems("Water")

    
def Acquired(item):
    inventory.append(item)
    


Intro()
Decide()
CheckPlease(Decide)
collect()
MoreItems()










