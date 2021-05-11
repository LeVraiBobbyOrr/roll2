import random
import diceRoll

def strToDiceRoll(diceInput):
    
    diceDecomp = diceStringDecomp(diceInput)   #decompose roll string
        
    diceAmount = int(diceDecomp[0])
    diceType = int(diceDecomp[1])

    diceResults = diceRollAddition(diceAmount, diceType)   #roll the dices

    printResults(diceResults, 1)      #print the results
    return diceResults
        
def decompStrIntoDice(rollStr):
    diceInputNoSpace = rollStr.replace(" ","")
    diceInputList = diceInputNoSpace.split("+")
    return diceInputList

def diceStringDecomp(dice):
    #decompose the string to recognize the amount of dice to roll and the dice type
    #dice : roll string like 1d4, 2d6, 3d8, YdX, etc.

    if isDiceRoll(dice) == False : return 0,dice
    else:
        diceType = ""
        diceAmount = ""
        d = int(0)
        for x in range(len(dice)):  #detect the amount of dice to roll
            if dice[x] == "d":      #look for the mark of 'd'
                d = int(x)
                break
            diceAmount = diceAmount + str(dice[x])
            
        for x in range(d+1, len(dice)):                 #detect the dice type
            diceType = diceType + str(dice[x])
            
        return diceAmount,diceType              

def diceRollAddition(diceAmount,diceType):
    #roll diceAmount times and record the results
    #diceAmount : number of roll to make
    #diceType: type of dice like d4, d6, dX etc.
    
    if diceAmount == 0:
        return [diceType]
    
    else:
        diceResults = [None]*diceAmount             #set the list dimension    
        for x in range(diceAmount):
            diceResults[x] = int(random.randint(1,int(diceType)))       #roll the dice
            
        return diceResults

def printResults(diceResults, total):
    #print the individual result of each dice and the sum
    #diceResults : list of dice results
    
    print("Roll : ", end ="      " )
    print(diceResults)
    if total != 0:
        print("Sum of roll :", end =" ")
        print(sum(diceResults))
    print("")

def isDiceRoll (diceRoll):
    #if 'd' is present, its a dice roll. Else, its a number
    
    if diceRoll.find('d') != -1: return True
    else: return False
        
while 1:
    try:
        print("********************************************")
        rollInput = "0"                             #input
        rollInput = str(input("Roll : "))
        print("")

        diceInputList = decompStrIntoDice(rollInput)

        totalResults = int(0)
        for x in range (len(diceInputList)):
            totalResults = totalResults + sum(strToDiceRoll(diceInputList[x]))

        print("TOTAL ROLL : ", end ="")   
        print(totalResults)
        print("")
        
    except ValueError:
        print("Invalid dice, try again.")
        print("Format : XXdYY")
        print ("example : 2d4, 1d20 + 1, 1d6 + 2d8 + 4")
        print("")
            
