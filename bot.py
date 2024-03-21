from discord.ext import commands
import discord
import random
from main import gameMechanics
botToken = "MTIyMDIzNTE2MDkyNzM0MjcwMg.G5L2GC.6U_ZEchOmxbTVQNBVXa48JJ6V4bWKYIoujEy00"
channelId = 1220236496057929859

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
balance = 2
###START HAND

@bot.command()
async def play(channelId):

    ##GETS PLAYER BET
    while True:
        
        await channelId.send("Hello. Please type how much money you'd like to bet")

        ###Checks for users response
        def check(m):
            return(  
                m.content
                and m.channel.id == channelId.channel.id
                and m.author == channelId.author
            )
                
        msg = await bot.wait_for("message", check=check)
        msg = int(msg.content)
        print(msg)
        ###CHECKS IF PLAYER HAS ENOUGH MONEY TO BET
        if msg < balance:
            betWithinLimits = True
            break
        else:
            await channelId.send("Sorry you do not have enough money to bet that much, please type !play to try again.")
            break 
    
    #STARTING TO PLAY HAND
    while betWithinLimits == True:
        deck = gameMechanics.deckShuffle()
        print(deck)
        break

    
      


    
bot.run(botToken)   