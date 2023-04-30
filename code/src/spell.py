class Rage:
    def __init__(self):
        self.spell = 5
    
    def giveRage(self):
        self.spell -= 1
        
class Heal:
    def __init__(self):
        self.spell = 5
        
    def giveHeal(self):
        self.spell -= 1