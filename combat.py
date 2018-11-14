#Logan Nelson
#10-18
import random

win=0
pHealth = 100
mHealth = 100
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")
choice = input("fight or run")

while choice == "fight":
    playerDamage = random.randrange(0,30)
    print ("you attack the trolls and did " , playerDamage , " damage, killing hundreds of trolls")
    mHealth -= playerDamage
    if mHealth > 0:
        monsterDamage = random.randrange(0,50)
        print("the trolls fight back doing ", monsterDamage, " damage")
        pHealth -= monsterDamage
    if pHealth <=0:
        print ("you have died")
        win = 0
        break
    elif mHealth <= 0:
        print ("you have killed all the trolls")
        win = 1
        break
    elif pHealth >=0 and mHealth >=0:
        print ("you have ",pHealth,"health")
        print ("the trolls have" ,mHealth,"health")
        choice = input ("fight or run ")
        if choice =="fight":
            print ("you attack again")
        elif choice == "run":
                break

if choice == "run":
    print("you are a coward")
if win ==0:
    print("game over")
else:
    print("you win")







        
