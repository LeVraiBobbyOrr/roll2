import random

class diceRoll:
    diceAmount = 0
    diceType = 0
    modifier = 0
    diceRolled = False
    
    diceRollStr = "0"
    
    diceRollResults = []
    diceRollTotalResults = 0
    
    def __init__(self, diceAmount, diceType, modifier):
        self.diceAmount = diceAmount
        self.diceType = diceType
        self.modifier = modifier    

    def diceRollToStr(self):
        if self.diceAmount == 0:
            self.diceRollStr = str(self.modifier)
        else:
            self.diceRollStr = str(self.diceAmount) + 'd' + str(self.diceType)
            if self.modifier !=0:
                self.diceRollStr = str(self.diceRollStr) + " + " + str(self.modifier)
        

    def printDiceRoll(self):
        self.diceRollToStr()
        print(self.diceRollStr)

    def diceRollAddition(self):
    #roll diceAmount times and record the results
    #diceAmount : number of roll to make
    #diceType: type of dice like d4, d6, dX etc.
    
        self.diceRollResults = [None]*self.diceAmount             #set the list dimension    
        for x in range(self.diceAmount):
            self.diceRollResults[x] = int(random.randint(1,int(self.diceType)))       #roll the dice

        self.diceRolled = True
        self.diceRollTotalResults = sum(self.diceRollResults) + self.modifier

   #def     
        
    def printRollResults(self):
        print(self.diceRollResults)
        
    def printTotalResults(self):
        print(self.diceRollTotalResults)

    

class rollResults(diceRoll):
    pass

"""
TEST
"""

x = diceRoll(2,6,3)

x.printDiceRoll()

x.diceRollAddition()
x.printRollResults()
x.printTotalResults()

print(sum(x.diceRollResults) + x.modifier)

del x
    
        
