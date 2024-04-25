
from PIL import Image 
from main import gameMechanics 
import os

def format_card_for_image(card) -> str:
    suit = card[1].lower()
    value = card[0].lower()

    return value + "_" + "of" + "_" + suit + ".png"

def place_cards_on_table(player_cards, dealer_cards, table, current_x_placement, card_width) -> None: 
    top_row = 50
    bottom_row = 275
    top_row_x = current_x_placement
    bottom_row_x = current_x_placement 
    
    for card in dealer_cards:
        table.paste(card, (top_row_x, top_row))
        top_row_x += card_width + 10
        
        
    for card in player_cards:
        table.paste(card, (bottom_row_x, bottom_row))
        bottom_row_x += card_width + 10
        
def card_image_example():
    deck = gameMechanics.deckShuffle()

    dealer_card = gameMechanics.dealNewCard(deck)
    player_card1 = gameMechanics.dealNewCard(deck)
    player_card2 = gameMechanics.dealNewCard(deck)

    # # Opening the primary image (used in background) 
    table = Image.open(r"./assets/table.png") 
    
    face_down_cards = Image.open(r"./assets/backofcard.png").resize((130, 210)) 
    stack_of_cards = Image.open(r"./assets/backofcard.png").resize((130, 210))
    
    dealer_card_image = Image.open(r"./assets/" + format_card_for_image(dealer_card)).resize((130, 210))
    player_card_image1 = Image.open(r"./assets/" + format_card_for_image(player_card1)).resize((130, 210))
    player_card_image2 = Image.open(r"./assets/" + format_card_for_image(player_card2)).resize((130, 210))

    # Displaying the image 
    #place_cards_on_table([player_card_image], [dealer_card_image], table, 25, 130)


    place_cards_on_table([player_card_image1, player_card_image2 ], [dealer_card_image, face_down_cards], table, 25, 130)


    table.paste(stack_of_cards, (600,50))  

    table.show()

def game(dealer_cards, player_cards):

    dealer_card = dealer_cards[0]
    #player_card1 = player_cards[0]
    #player_card2 = player_cards[1]

    # # Opening the primary image (used in background) 
    table = Image.open(r"./assets/table.png") 
    
    face_down_cards = Image.open(r"./assets/backofcard.png").resize((130, 210)) 
    stack_of_cards = Image.open(r"./assets/backofcard.png").resize((130, 210))
    
    player_card_images = []
    dealer_card_images = []

    dealer_card_image = Image.open(r"./assets/" + format_card_for_image(dealer_card)).resize((130, 210))

    for x in player_cards:
        player_card_images.append(Image.open(r"./assets/" + format_card_for_image(x)).resize((130, 210)))
    
    for x in dealer_cards:
        dealer_card_images.append(Image.open(r"./assets/" + format_card_for_image(x)).resize((130, 210)))


    # Displaying the image 
    #place_cards_on_table([player_card_image], [dealer_card_image], table, 25, 130)


    place_cards_on_table([player_card_images[x] for x in range(len(player_card_images))], [dealer_card_image, face_down_cards], table, 25, 130)


    table.paste(stack_of_cards, (600,50))  
    
    pathname = "./temp/table.png" 
    
    table.save(pathname)
        
    return pathname
    
    


def endgame_image(dealer_cards, player_cards):

    # # Opening the primary image (used in background) 
    table = Image.open(r"./assets/table.png") 
    
    stack_of_cards = Image.open(r"./assets/backofcard.png").resize((130, 210))
    
    player_card_images = []
    dealer_card_images = []

    for x in player_cards:
        player_card_images.append(Image.open(r"./assets/" + format_card_for_image(x)).resize((130, 210)))
    
    for x in dealer_cards:
        dealer_card_images.append(Image.open(r"./assets/" + format_card_for_image(x)).resize((130, 210)))


    # Displaying the image 
    #place_cards_on_table([player_card_image], [dealer_card_image], table, 25, 130)


    place_cards_on_table([player_card_images[x] for x in range(len(player_card_images))], [dealer_card_images[x] for x in range(len(dealer_card_images))], table, 25, 130)


    table.paste(stack_of_cards, (600,50))  

    # table.show()
    pathname = "./temp/table.png"
    
    table.save(pathname)


#Change this to enable testing
test = False

#Card image testing
while test == True:
    deck = gameMechanics.deckShuffle()

    playerCards = [] 
    dealerCards = []

    playerCards.append(gameMechanics.dealNewCard(deck))
    playerCards.append(gameMechanics.dealNewCard(deck))


    dealerCards.append(gameMechanics.dealNewCard(deck))
    dealerCards.append(gameMechanics.dealNewCard(deck))

    game(dealerCards, playerCards)