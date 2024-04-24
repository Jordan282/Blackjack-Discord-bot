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

                
        

#Change this value to true for testing
testing = False

#Ace tester
while testing == True:
    deck = gameMechanics.deckShuffle()
    dealerCards = []
    playerCards = []

    #dealerCards.append(gameMechanics.dealNewCard(deck))
    #dealerCards.append(gameMechanics.dealNewCard(deck))
    #playerCards.append(gameMechanics.dealNewCard(deck))
    #playerCards.append(gameMechanics.dealNewCard(deck))

    dealerCards.append(("Ace", "Spades"))
    dealerCards.append(("Ace", "Spades"))
    playerCards.append(("Ace", "Spades"))
    playerCards.append(("Ace", "Spades"))

    playerScore = 0
    for card in playerCards:
        newPlayerScore = gameMechanics.assignCardValues(card, playerScore)
        playerScore += newPlayerScore

    dealerScore = 0
    for card in dealerCards:
        newDealerScore = gameMechanics.assignCardValues(card, dealerScore)
        dealerScore += newDealerScore


    print(playerScore)
    print(dealerScore)

    input("Enter for new card")
    playerCards.append(gameMechanics.dealNewCard(deck))
    dealerCards.append(gameMechanics.dealNewCard(deck))

    print(playerCards)
    print(dealerCards)
    print(playerScore)
    print(dealerScore)
    input()

    playerScore = 0
    for card in playerCards:
        newPlayerScore = gameMechanics.assignCardValues(card, playerScore)
        playerScore += newPlayerScore

    dealerScore = 0
    for card in dealerCards:
        newDealerScore = gameMechanics.assignCardValues(card, dealerScore)
        dealerScore += newDealerScore

    print(playerCards)
    print(dealerCards)
    print(playerScore)
    print(dealerScore)

