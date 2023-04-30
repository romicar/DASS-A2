from sqlalchemy import false, true
from village import *
from king import *
from input import *
from replay import *
from barbarians import *
from spell import *
from os import system
import math

gameOver = false

v = village()

v.setBoundary()
v.spawningPoints()

B1 = Building(v.display, 100, 18, Back.WHITE)
B1.createBuilding()
B2 = Building(v.display, 10, 6, Back.CYAN)
B2.createBuilding()
B3 = Building(v.display, 170, 9, Back.RED)
B3.createBuilding()

# v.townHall()

H1 = Hut(v.display, 32, 5, Back.RESET, Back.YELLOW)
H1.createHut()
H2 = Hut(v.display, 10, 23, Back.RESET, Back.LIGHTWHITE_EX)
H2.createHut()
H3 = Hut(v.display, 40, 30, Back.RESET, Back.BLUE)
H3.createHut()
H4 = Hut(v.display, 150, 15, Back.RESET, Back.CYAN)
H4.createHut()
H5 = Hut(v.display, 190, 30, Back.RESET, Back.WHITE)
H5.createHut()

C1 = Canon(v.display, 30, 15)
C1.createCanon()
C2 = Canon(v.display, 140, 25)
C2.createCanon()

K = King(v.display, 65, 45)
K.createKing()

W1 = Wall(v.display, 16, 35)
W1.createWall()
W2 = Wall(v.display, 80, 38)
W2.createWall()
W3 = Wall(v.display, 150, 34)
W3.createWall()
W4 = Wall(v.display, 55, 32)
W4.createWall()

# obstacles = {"walls": [(W1,16, 35), (W2,80, 38), (W3,150, 34), (W4,55, 32)], "huts": [(H1,32, 5), (H2,10, 23), (H3,40, 30), (
#     H4,150, 15), (H5,190, 30)], "buildings": [(B1,100, 18), (B2,10, 6), (B3,170, 9)], "canons": [(C1,30, 15), (C2,140, 25)]}

obstacles = [(W1,16, 35), (W2,80, 38), (W3,150, 34), (W4,55, 32),(H1,32, 5), (H2,10, 23), (H3,40, 30), (
    H4,150, 15), (H5,190, 30),(B1,100, 18), (B2,10, 6), (B3,170, 9),(C1,30, 15), (C2,140, 25)]

T1, T2, T3 = [], [], []

t1 = createTroop(v.display, 26, 42, T1)
t2 = createTroop(v.display, 100, 42, T2)
t3 = createTroop(v.display, 180, 42, T3)

count = 0
R = replay()
def findClosestBuilding(buildings, T):
    count = 100000000
    b = 0
    for i in buildings:
        if(count > (T.x - i.x)**2+(T.y-i.y)**2):
            count = (T.x - i.x)**2+(T.y-i.y)**2
            b = i
    K.dist = math.sqrt(count)
    return b

B = 0
lflag, cflag, rflag = false, false, false
vill = [B1, B2, B3, H1, H2, H3, H4, H5, C1, C2]
b = [B1, B2, B3, H1, H2, H3, H4, H5, C1, C2]
while gameOver == false:
    _ = system('clear')
    print("\n".join(["".join(row)
          for row in v.display]), Style.RESET_ALL, end='')
    print()
        
    keyInput = Get().get_input(timeout=0.1)
    if keyInput == "q":
        gameOver = true
    if keyInput == "w" or keyInput == "a" or keyInput == "s" or keyInput == "d":
        K.movement(keyInput)
    if keyInput == "l":
        lflag, cflag, rflag = true, false, false
        t1.createArrayBarbarian()
    
    if keyInput == "c":
        lflag, cflag, rflag = false, true, false
        t2.createArrayBarbarian()
        B = findClosestBuilding(
            [B1, B2, B3, H1, H2, H3, H4, H5, C1, C2], T2[0])
    if keyInput == "r":
        lflag, cflag, rflag = false, false, true
        t3.createArrayBarbarian()
        B = findClosestBuilding(
            [B1, B2, B3, H1, H2, H3, H4, H5, C1, C2], T3[0])
    if keyInput == 'h':
        Heal().giveHeal()
        K.Health = int(K.Health*1.5)
        K.createKing()
        if K.Health > 100:
            K.Health = 100
        if(lflag == true):
            t1.updateHealth()
        elif cflag == true:
            t2.updateHealth()
        else:
            t3.updateHealth()
            
    if keyInput == 'i':
        Rage().giveRage()
        K.damage *=2
        K.speed *=2
        K.createKing()
        if(lflag == true):
            t1.updateDamage()
        elif cflag == true:
            t2.updateDamage()
        else:
            t3.updateDamage()
            
    if keyInput == 'R':
        for i in R.stk:
            _ = system('clear')
            time.sleep(1)
            print(i)


    if(lflag == true):
        B = findClosestBuilding(vill,T1[0])
        t1.update(B,obstacles,vill)
    elif cflag == true:
        B = findClosestBuilding(vill,T2[0])
        t2.update(B,obstacles,vill)
    elif(rflag == true):
        B = findClosestBuilding(vill,T3[0])
        t3.update(B,obstacles,vill)
        
    K.attack(findClosestBuilding(vill,K),vill)
    
    if(len(vill) == 0):
        gameOver = true
        print("GAME OVER")
        
    H1.updateHut()
    H2.updateHut()
    H3.updateHut()
    H4.updateHut()
    H5.updateHut()
    C1.updateCanon()
    C2.updateCanon()
    B1.updateBuilding()
    B2.updateBuilding()
    B3.updateBuilding()
    
    R.stk.append(v.display)
    
    
