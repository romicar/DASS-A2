from colorama import Back, Fore,Style
import math

class King:
    def __init__(self,arr,x,y):
        self.arr = arr
        self.x = x
        self.y = y
        self.Health = 100
        self.speed = 1
        self.damage = 10
        self.dist = 0
        
    def createKing(self):
        for i in range(self.x-4,self.x-4+int(self.Health/10)):
            if self.Health > 50:
                self.arr[self.y-2][i] = f"{Back.GREEN} {Back.RESET}"
            elif self.Health > 20:
                self.arr[self.y-2][i] = f"{Back.YELLOW} {Back.RESET}"
            else:
                self.arr[self.y-2][i] = f"{Back.RED} {Back.RESET}"
        for i in range(self.x-4+int(self.Health/10),self.x-4+10):
            self.arr[self.y-2][i] = f"{Back.RESET} {Back.RESET}"
            
        if(self.Health > 0):
            self.arr[self.y][self.x] = f'{Back.LIGHTYELLOW_EX}{Fore.RED}+{Fore.RESET}{Back.RESET}'
            self.arr[self.y+1][self.x] = '0'
            self.arr[self.y+2][self.x-1] = f'{Back.BLUE}({Back.RESET}'
            self.arr[self.y+2][self.x] = f'{Back.GREEN}|{Back.RESET}'
            self.arr[self.y+2][self.x+1] = f'{Back.BLUE}){Back.RESET}'
            self.arr[self.y+3][self.x-1] = '/'
            self.arr[self.y+3][self.x+1] = '\\'
        else:
            self.arr[self.y][self.x] = " "
            self.arr[self.y+1][self.x] = " "
            self.arr[self.y+2][self.x-1] = " "
            self.arr[self.y+2][self.x] = " "
            self.arr[self.y+2][self.x+1] = " "
            self.arr[self.y+3][self.x-1] = " "
            self.arr[self.y+3][self.x+1] = " "
            
    def updateKing(self,x,y):
        for i in range(self.x-4,self.x-4+int(self.Health/10)):
            if self.Health > 50:
                self.arr[self.y-2][i] = f" "
            elif self.Health > 20:
                self.arr[self.y-2][i] = f" "
            else:
                self.arr[self.y-2][i] = f" "
        for i in range(self.x-4+int(self.Health/10),self.x-4+10):
            self.arr[self.y-2][i] = f" "
            
        
        self.arr[self.y][self.x] = " "
        self.arr[self.y+1][self.x] = " "
        self.arr[self.y+2][self.x-1] = " "
        self.arr[self.y+2][self.x] = " "
        self.arr[self.y+2][self.x+1] = " "
        self.arr[self.y+3][self.x-1] = " "
        self.arr[self.y+3][self.x+1] = " "
        
        self.x = x
        self.y = y
        
        self.createKing()
        
    def attack(self,B,vill):
        if self.dist < 9:
            B.Health -= self.damage
            if B.Health == 0:
                vill.remove(B)
    
    def movement(self,key):
        occupyflag = 0
        if(key == "w"):
            for i in range(self.x-5,self.x+7):
                if(self.arr[self.y-3][i] != " "):
                    occupyflag = 1
                    # self.attack(i,self.y-3)
            if(occupyflag == 0):
                self.updateKing(self.x,self.y-self.speed)
        if(key == "a"):
            for i in range(self.y-3,self.y+5):
                if(self.arr[i][self.x-5] != " "):
                    occupyflag = 1
                    # self.attack(self.x-5,i)
            if(occupyflag == 0):
                self.updateKing(self.x-self.speed,self.y)
        if(key == "s"):
            for i in range(self.x-5,self.x+7):
                if(self.arr[self.y+4][i] != " "):
                    occupyflag = 1
                    # self.attack(i,self.y+4)
            if(occupyflag == 0):
                self.updateKing(self.x,self.y+self.speed)
        if(key == "d"):
            for i in range(self.y-3,self.y+5):
                if(self.arr[i][self.x+6] != " "):
                    occupyflag = 1
                    # self.attack(self.x+6,i)
            if(occupyflag == 0):
                self.updateKing(self.x+self.speed,self.y)
    