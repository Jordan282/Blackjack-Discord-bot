import random
import json

class gameMechanics:

    def deckShuffle():
        cardsList = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        cardSuits = ["Diamonds", "Spades", "Hearts", "Clubs"]
        deck = [(card, suit) for card in cardsList for suit in cardSuits]
        random.shuffle(deck)
        ##TEST CODE
        #print(deck)
        return deck

    def dealNewCard(deck):
        
        newCard = deck.pop()

        return newCard
    

    def assignCardValues(card, score):
        if card[0] in ["Jack", "Queen", "King"]:
            return 10
        elif card[0] == "Ace":
            #print(score)
            #print(card)
            if score < 11:
                return 11
            else:
                return 1
        
        else:
            return int(card[0])


    def readFile():
        with open ("balances.json", "r") as openfile:
            jsonObject = json.load(openfile)
            #print(jsonObject)
            #print(type(jsonObject))
            return jsonObject

    def writeFile(playerBalances):
        with open ("balances.json", "w") as outfile:
            jsonString = json.dump(playerBalances, outfile)
    
    def addNewBalance(msgAuthor):
        balanceDict = gameMechanics.readFile()
        #print(balanceDict)
        balanceDict[msgAuthor] = 100
        #print(balanceDict)
        with open("balances.json", "w") as outfile:
            jsonString = json.dump(balanceDict, outfile)

    def calcNewBalanceLoss(msgAuthor, balance, bet):
        balanceDict = gameMechanics.readFile()
        total = balance - bet
        #print(balanceDict
        balanceDict[msgAuthor] = total
        #print(balanceDict)
        with open("balances.json", "w") as outfile:
            jsonString = json.dump(balanceDict, outfile)

    def calcNewBalanceWin(msgAuthor, balance, bet):
        balanceDict = gameMechanics.readFile()
        total = balance + bet
        #print(balanceDict)
        balanceDict[msgAuthor] = total
        #print(balanceDict)
        with open("balances.json", "w") as outfile:
            jsonString = json.dump(balanceDict, outfile)

    def checkPlayerBalance(playerId):
        balanceDict = gameMechanics.readFile()
        playerBalance = balanceDict[str(playerId)]
        return playerBalance

    def aceList(card):
        if card[0] in ["Ace"]:
            return 1
        else:
            return 0
    
    def revalueAces(score, aces):
        dictionary = {"aces": aces, "score": score}
        #print(dictionary)
        if score > 21:
            if aces > 0:
                dictionary["score"] = score - 10
                dictionary["aces"] = aces - 1
                return dictionary
                
                
        





            
#playerBalances = {
    #1:1
#}

#msgAuthor = 123

#gameMechanics.writeFile(playerBalances)
##gameMechanics.addNewBalance(msgAuthor)
    
#gameMechanics.checkPlayerBalance("362001727714623489")


        
    


