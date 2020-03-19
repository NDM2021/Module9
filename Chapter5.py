inventory = []

health = 200
playerDamage = 70
creatureHealth = 200
creatureDamage = 25

def main():
    print("Chapter Five")

main()

def ForwardCast():
    print("Sun is setting, and the creature are more bloodthirsty than the last.")
    print("Creature grows stronger as it gets hungrier")
    print("Player is gearing up to fight and kill the creature.")
    print("The creature is hungry and will eat through anyone or anything that defies it")
    print("It will devour every single one that faces it")
    print("You have your weapons ready. You are walking through the woods")
    print("The officers have came to help")
    print("Your sword in one hand and speak and the other")
    print("You hear the creature's loud roah")
    print("The creature launches out at you. Planning to take off your head")



def Attack():
    global health
    global creatureHealth
    global creatureDamage
    health = health - creatureDamage

def KeepAttacking():
    print("The creature launches at you again in an attempt to rip your head clean off!")
    Attack()
    print("You have", health, "left")
    print("The creatures attack again, only trying to kill you slow")
    Attack()
    print("You have", health, "left")


def Tiles():
    print("You are not bleeding, just yet")
    print("The creature didn't do alot of damage to you")
    print("The officers are shooting it but they aren't do any damage")
    print("You try to find the creature's weakness and attack it")

def ComeOn():
    global health
    global playerDamage
    global creatureHealth
    global creatureDamage
    creatureHealth = creatureHealth - playerDamage


def AttackMore():
    print("you attack the creature weak point")
    ComeOn()
    print("The creature have", creatureHealth,"left")
    print("You keep attacking it")
    ComeOn()
    print("The creature have", creatureHealth, "left")

def BreakTime():
    print("The creature is getting overwhelmed, losing health")
    print("The creature dies, only rising to be stronger")
    print("The creature transformed and grew claws")
    print("You attack the creature once more")

def finalBlow():
    global health
    global playerDamage
    global creatureHealth
    global creatureDamage
    creatureHealth = creatureHealth - playerDamage

def LetSee():
    print("That was critical blow to the creature")
    finalBlow()
    print("The creature have", creatureHealth, "left")
    print("You attempt to attack again")
    print("The creature have", creatureHealth, "left")

def Finally():
    print("The creature is bleeding out")
    print("The creature slowly dies")
    print("You've killed the creature")
    print("You've collected rewards")

def Rewarding():
    global inventory
    print("You've killed the creature and collected rewards")
    Rewarding == input
    if Rewarding == "Yes":
        Rewarding("$500")

    def collector(item):
        inventory.append(item)


ForwardCast()
Attack()
KeepAttacking()
Tiles()
ComeOn()
AttackMore()
BreakTime()
finalBlow()
LetSee()
Finally()
Rewarding()    




