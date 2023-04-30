from colorama import Back,Fore,Style
import time

class Barbarian:
    def __init__(self,arr,x,y):
        self.arr = arr
        self.x = x
        self.y = y
        self.Health = 100
        self.Damage = 1
        self.speed = 1
        
    def createBarbarian(self):
        color = Back.GREEN
        if(self.Health >= 20 and self.Health < 50):
            color = Back.YELLOW
        if(self.Health < 20):
            color = Back.RED
        self.arr[self.y][self.x] = f"{color} {Back.RESET}"
        self.arr[self.y][self.x+1] = f"{color} {Back.RESET}"
        
        
class Troops(Barbarian):
    def __init__(self,arr,x,y):
        Barbarian.__init__(self,arr,x,y)
        
    def attackTroop(self):
        pass
        
    def updateTroop(self,B,vill):
        self.arr[self.y][self.x] = " "
        self.arr[self.y][self.x+1] = " "
        
        x1,y1 = self.x,self.y
        
        if(self.x != B.x and self.y != B.y):
            if(self.x < B.x):
                self.x+=1
            if self.x > B.x:
                self.x -= 1
            if(self.y < B.y):
                self.y +=1
            if self.y > B.y:
                self.y -= 1
        elif self.x == B.x and self.y != B.y:
            if self.y < B.y:
                self.y+=1
            if self.y > B.y:
                self.y -= 1
        elif self.x != B.x and self.y == B.y:
            if self.x < B.x:
                self.x+=1
            if self.x > B.x:
                self.x -= 1
        
        if(self.arr[self.y][self.x] == f"{Back.BLACK}#{Back.RESET}" or self.arr[self.y][self.x] == f"{Back.YELLOW}#{Back.RESET}"):
            time.sleep(1)
            pass
        elif(self.arr[self.y][self.x] != " "):
            self.x,self.y = x1,y1
            B.Health -= self.Damage
            if B.Health == 0:
                vill.remove(B)
    
        self.createBarbarian()
        
    def updateBHealth(self):
        self.Health = int(self.Health * 1.5)
        if self.Health > 100:
            self.Health = 100
        self.createBarbarian()
            
    def updateBDamage(self):
        self.Damage *= 2
        self.speed *=2
        self.createBarbarian()
        
      
# class Attack():
#     def __init__(self,arr,obstacles,x,y):
#         self.arr = arr
#         self.x = x
#         self.y = y
#         self.obstacles = obstacles
        
#     def isWallsAttacked(self):
#         # self.arr[4][4] = self.y
#         # self.arr[4][5] = self.obstacles[0][2]
#         for i in self.obstacles:
#             if((self.x+1 == i[1] and self.y == i[2]) or (self.x-1 == i[1] and self.y == i[2]) or (self.x == i[1] and self.y+1 == i[2]) or (self.x+1 == i[1] and self.y-1 == i[2])):
#                 return i[0]                
        
class createTroop():
    def __init__(self,arr,x,y,T):
        self.arr = arr
        self.x = x
        self.y = y
        self.T = T
        
    def createArrayBarbarian(self):
        self.T.append(Troops(self.arr,self.x,self.y))
        self.T.append(Troops(self.arr,self.x-2,self.y+2))
        self.T.append(Troops(self.arr,self.x+2,self.y+2))
        self.T.append(Troops(self.arr,self.x-4,self.y+4))
        self.T.append(Troops(self.arr,self.x,self.y+4))
        self.T.append(Troops(self.arr,self.x+4,self.y+4))
        self.T.append(Troops(self.arr,self.x-6,self.y+6))
        self.T.append(Troops(self.arr,self.x,self.y+6))
        self.T.append(Troops(self.arr,self.x+6,self.y+6))
        
        for i in self.T:
            i.createBarbarian()
            
    def update(self,B,obstacles,vill):
        for i in self.T:
            i.updateTroop(B,vill)
            # w = Attack(self.arr,obstacles,i.x,i.y)
            
            # if w.isWallsAttacked() != None:
            #     w.Health = 0
                
    def updateHealth(self):
        for i in self.T:
            i.updateBHealth()
            
    def updateDamage(self):
        for i in self.T:
            i.updateBDamage()
                

        
        