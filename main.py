import random

class gameMechanics:

    def deckShuffle():
        cardsList = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        cardSuits = ["Diamonds", "Spades", "Hearts", "Clubs"]
        deck = [(card, suit) for card in cardsList for suit in cardSuits]
        random.shuffle(deck)
        ##TEST CODE
        #print(deck)
        return deck
