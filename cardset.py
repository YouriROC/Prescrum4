import pygame as pg
import random


def random_color():
    # return a random RGB value
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,100)
    return (r, g, b)


# initialise pygame
pg.init()
clock = pg.time.Clock()

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 750
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Name and icon
icon = pg.image.load("images/memorylogo.png")
pg.display.set_icon(icon)
pg.display.set_caption("Memory Game")

# load and store the card images
filenames = [
        'images/cards/cardA.png',
        'images/cards/cardB.png',
        'images/cards/cardC.png',
        'images/cards/cardD.png',
        'images/cards/cardE.png',
        'images/cards/cardF.png',
        'images/cards/cardG.png',
        'images/cards/cardH.png',
        'images/cards/cardI.png',
        'images/cards/cardJ.png',
        'images/cards/cardA.png',
        'images/cards/cardB.png',
        'images/cards/cardC.png',
        'images/cards/cardD.png',
        'images/cards/cardE.png',
        'images/cards/cardF.png',
        'images/cards/cardG.png',
        'images/cards/cardH.png',
        'images/cards/cardI.png',
        'images/cards/cardJ.png'
        # etc.
        # place all your card image filenames in this list
        ]
try:
    # try loading the images from files
    card_images = [pg.image.load(f).convert_alpha() for f in filenames]
except Exception as e:
    print(e)
    # if loading fails, construct some dummy images
    card_images = []
    for i in range(20):
        s = pg.Surface((48, 64))
        s.fill(random_color())
        card_images.append(s)

# make a card class for displaying and possible interaction etc
class Card():
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

# create a bunch of card objects from the image
cards = [Card(img) for img in card_images]
# shuffle the card list in place
random.shuffle(cards)
    




# set each card's position on the screen
horizontal_spacing =120
vertical_spacing = 100
horizontal_indent = 550
vertical_indent = 90
marvertical_indent = 250

for i, card in enumerate(cards):
    pos_x = horizontal_indent + i % 5 * horizontal_spacing
    pos_y = marvertical_indent + i // 5 * vertical_spacing
    card.rect.center = (pos_x, pos_y)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    clock.tick(30)
    

    bg_img = pg.image.load("images/background.png")  # loads image 
    screen.blit(bg_img, (1, 1)) 

    # draw the cards
    for c in cards:
        c.draw(screen)
    
    pg.display.flip()
    