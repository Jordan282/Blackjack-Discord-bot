from discord.ext import commands
import discord
import random
from main import gameMechanics
from hidden import hidden
from render_cards import *

botToken = hidden.botToken
channelId = hidden.channelId

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
###START HAND

async def handle_photo(bot, pathname):
    
    await bot.send(file=discord.File(pathname))
    # await os.remove("")
    

@bot.command()
async def play(channelId):

    ##GETS PLAYER BET
    while True:
        
        betWithinLimits = False
        jumpToPlayerPhase = False
        jumpToDealerPhase = False
        jumpToGameResult = False
        

        await channelId.send("Hello. Please type how much money you'd like to bet")

        ###Checks for users response
        def check(m):
            return(  
                m.content
                and m.author.id
                and m.channel.id == channelId.channel.id
                and m.author == channelId.author
            )

              
        msg = await bot.wait_for("message", check=check)
        msgAuthor = str(msg.author.id)
        bet = int(msg.content)
        
        balance = gameMechanics.readFile().get(msgAuthor)

        #print(type(balance))

        #Adds new account if one doesnt exist 
        if type(balance) != int:
            gameMechanics.addNewBalance(msgAuthor)
            balance = int(gameMechanics.readFile().get(msgAuthor))
        
        #print(msgAuthor)
        #print(balance)
        #print(type(msg))
        #print(type(balance))
        #print(bet)

        ###CHECKS IF PLAYER HAS ENOUGH MONEY TO BET
        if bet <= balance:
            betWithinLimits = True
            break
        else:
            await channelId.send("Sorry you do not have enough money to bet that much, please type !play to try again.")
            break 
    
    #Starting new hand
    while betWithinLimits == True:
        playerScore = 0
        dealerScore = 0
        deck = gameMechanics.deckShuffle()
        dealerCards = []
        playerCards = []
        tempPlayerCards = []
        tempDealerCards = []

        
        dealerCards.append(gameMechanics.dealNewCard(deck))
        dealerCards.append(gameMechanics.dealNewCard(deck))
        playerCards.append(gameMechanics.dealNewCard(deck))
        playerCards.append(gameMechanics.dealNewCard(deck))


        playersFirstCard = playerCards[0]
        dealersFirstCard = dealerCards[0]
    

        #if playersFirstCard[0] == "Ace":
            #playerCards.reverse()

        #if dealersFirstCard[0] == "Ace":
            #dealerCards.reverse()
    


        game(dealerCards, playerCards)
        await handle_photo(channelId, "./temp/table.png")


        #await channelId.send("Dealers face up card is below (Dealer has 2 cards... one is just not visible)")
        #await channelId.send(dealerCards[0])
        #await channelId.send("You have the cards below")
        #await channelId.send(playerCards)
        
        tempPlayerCards = playerCards.copy()
        gameMechanics.rearrangeCards(tempPlayerCards)
        playerScore = 0
        for card in tempPlayerCards:
            newPlayerScore = gameMechanics.assignCardValues(card, playerScore)
            playerScore += newPlayerScore

        tempDealerCards = dealerCards.copy()
        gameMechanics.rearrangeCards(tempDealerCards)
        dealerScore = 0
        for card in tempDealerCards:
            newDealerScore = gameMechanics.assignCardValues(card, dealerScore)
            dealerScore += newDealerScore

        #playerAces = sum(gameMechanics.aceList(card) for card in playerCards)
        #dealerAces = sum(gameMechanics.aceList(card) for card in dealerCards)
        
        #print(playerAces)
        #print(dealerAces)

        
        break


    
    #Checking for a player blackjack
    if playerScore == 21:
        if dealerScore == 21:
            #await channelId.send("Sorry tough luck. You and the dealer both have blackjack. It's a push")
            jumpToGameResult = True
        else:
            #await channelId.send("You have a blackjack, you win!")
            jumpToGameResult = True

    #Checking for a dealer blackjack        
    elif dealerScore == 21:
        #await channelId.send("Dealer has blackjack, you lose.")
        jumpToGameResult = True

    else:
        jumpToPlayerPhase = True
    
    #If no one has a blackjack we continue the hand as normal
    #Hit or stand segment of the game
    while jumpToPlayerPhase == True:
        await channelId.send("Would you like to hit or stand?")
        msg = await bot.wait_for("message", check=check)
        msg = msg.content.lower()

        #Player hit logic
        if msg == "hit":
            playerCards.append(gameMechanics.dealNewCard(deck))
            game(dealerCards, playerCards)
            await handle_photo(channelId, "./temp/table.png")

            tempPlayerCards = playerCards.copy()
            gameMechanics.rearrangeCards(tempPlayerCards)
            playerScore = 0
            for card in tempPlayerCards:
                newPlayerScore = gameMechanics.assignCardValues(card, playerScore)
                playerScore += newPlayerScore

            if playerScore > 21:
                jumpToDealerPhase = False
                jumpToPlayerPhase = False
                jumpToGameResult = True
                #await channelId.send("You busted, you lose")
                break
            else:
                #await channelId.send("Dealers face up card is below (Dealer has 2 cards... one is just not visible)")
                #await channelId.send(dealerCards[0])
                #await channelId.send("You have the cards below")
                #await channelId.send(playerCards)
                continue

        elif msg == "stand":
            jumpToPlayerPhase = False
            jumpToDealerPhase = True
            break   
        else:
            continue
    
    #Give dealer their cards
    while jumpToDealerPhase == True:
        tempDealerCards = dealerCards.copy()
        gameMechanics.rearrangeCards(tempDealerCards)
        dealerScore = 0
        for card in tempDealerCards:
            newDealerScore = gameMechanics.assignCardValues(card, dealerScore)
            dealerScore += newDealerScore

        if dealerScore < 17:
            dealerCards.append(gameMechanics.dealNewCard(deck))
            continue
        elif dealerScore > 21:
            #await channelId.send("Dealer has busted, you win!")
            jumpToDealerPhase = False
            jumpToGameResult = True
            break
        else:
            jumpToDealerPhase = False
            jumpToGameResult = True
            break
    
    #Game result
    while jumpToGameResult == True:

        endgame_image(dealerCards, playerCards)
        await handle_photo(channelId, "./temp/table.png")

        
        if playerScore > 21:
            #await channelId.send("Dealer has the cards below")
            #await channelId.send(dealerCards)
            #await channelId.send(dealerScore)
            #await channelId.send("You have the cards below")
            ##await channelId.send(playerCards)
            #await channelId.send(playerScore)
            await channelId.send("You busted, you lose")
            gameMechanics.calcNewBalanceLoss(msgAuthor, balance, bet)
            break   

        elif dealerScore > 21:
            #await channelId.send("Dealer has the cards below")
            #await channelId.send(dealerCards)
            #await channelId.send(dealerScore)
            #await channelId.send("You have the cards below")
            #await channelId.send(playerCards)
            #await channelId.send(playerScore)
            await channelId.send("Dealer busted, you win")
            gameMechanics.calcNewBalanceWin(msgAuthor, balance, bet)
            break

        elif dealerScore > playerScore:
            #await channelId.send("Dealer has the cards below")
            #await channelId.send(dealerCards)
            #await channelId.send(dealerScore)
            #await channelId.send("You have the cards below")
            #await channelId.send(playerCards)
            #await channelId.send(playerScore)
            await channelId.send("Dealer has a higher score, you lose")
            gameMechanics.calcNewBalanceLoss(msgAuthor, balance, bet)
            break

        elif playerScore > dealerScore:
            #await channelId.send("Dealer has the cards below")
            #await channelId.send(dealerCards)
            #await channelId.send(dealerScore)
            #await channelId.send("You have the cards below")
            #await channelId.send(playerCards)
            #await channelId.send(playerScore)
            await channelId.send("You have a higher score, you win")
            gameMechanics.calcNewBalanceWin(msgAuthor, balance, bet)
            break

        elif playerScore == dealerScore:
            #await channelId.send("Dealer has the cards below")
            #await channelId.send(dealerCards)
            #await channelId.send(dealerScore)
            #await channelId.send("You have the cards below")
            #await channelId.send(playerCards)
            #await channelId.send(playerScore)
            await channelId.send("You and the dealer have the same score, it's a push")
            break

    
    #print("loop has been broken")
    #print(playerCards)
    #print(playerScore)
      
@bot.command()
async def balance(channelId):
    #print("Sup")
    #print(channelId.author.id)
    playerBalance = gameMechanics.checkPlayerBalance(channelId.author.id)
    await channelId.send(playerBalance)

@bot.command()
async def buy(channelId):
    playerBalance = gameMechanics.checkPlayerBalance(channelId.author.id)
    if playerBalance == 0:
        gameMechanics.addNewBalance(channelId.author.id)




bot.run(botToken)       