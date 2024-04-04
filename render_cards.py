
from PIL import Image 
from main import gameMechanics  

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
    player_card = gameMechanics.dealNewCard(deck)

    # # Opening the primary image (used in background) 
    table = Image.open(r"./assets/table.png") 
    
    face_down_cards = Image.open(r"./assets/backofcard.png").resize((130, 210)) 
    stack_of_cards = Image.open(r"./assets/backofcard.png").resize((130, 210))
    
    dealer_card_image = Image.open(r"./assets/" + format_card_for_image(dealer_card)).resize((130, 210))
    player_card_image = Image.open(r"./assets/" + format_card_for_image(player_card)).resize((130, 210))

    # Displaying the image 
    place_cards_on_table([player_card_image], [dealer_card_image], table, 25, 130)


    place_cards_on_table([player_card_image, ], [dealer_card_image, face_down_cards], table, 25, 130)


    table.paste(stack_of_cards, (600,50))  

    table.show()
    
card_image_example()