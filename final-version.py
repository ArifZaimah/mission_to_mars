import os
import time

print("How much food do you to bring during your travel?")
food = float(input("Ton(s) of food:"))
print("How much water do you to bring during your travel?")
water = float(input("Kilolitre(s) of water:"))

def rocket():
  distanceFromTop = 20
  while distanceFromTop > 0:
    print("\n           _  _")
    print("\n         /      \ ")
    print("\n        |  MARS  |")
    print("\n         \ _  _ /")    
    print("\n" * distanceFromTop)
    print("           /\ ")
    print("           ||")
    print("           ||")
    print("          /||\ ")
    print("\n")
    print("arriving at destination in "+str(13.463*distanceFromTop)+" millions km")
    print("food left is "+str(food/20*distanceFromTop)+" tons")
    print("water left is "+str(water/20*distanceFromTop)+" kilolitres")
    time.sleep(1)
    os.system("cls")
    distanceFromTop -= 1
    
rocket()
print("YOU HAVE ARRIVE ON MARS")
print("You have "+str(food/20)+" tons of food and "+str(water/20)+" kilolitres of water left to survive before finding a new resources")

    
    

  
  

