import pygame as pg
import pygame.freetype
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
 
SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 950
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
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
 
 
# image of the card back
cardback = pg.image.load('images/cards/card_back.png')
 
cards_flipped = 0
 
 
# make a card class for displaying and possible interaction etc
class Card():
    def __init__(self, image):
        self.frontside = image.copy()
        self.image = self.frontside
        self.rect = image.get_rect()
        self.flipped = False
       
       
    def update(self, mouse_clicked):
        # detect the mouse position
        if mouse_clicked:
            mpos = pg.mouse.get_pos()
            if self.rect.collidepoint(mpos):
                self.flipped = True
                global cards_flipped
                cards_flipped += 1
 
        # set the card's image depending on if it is flipped or not
        if not self.flipped:
            self.image = cardback.copy()
        else:
            self.image = self.frontside
        if cards_flipped >= 2:
            self.flipped = False
            cards_flipped = 0
   
       
    def draw(self, screen):
        screen.blit(self.image, self.rect)

 
# create a bunch of card objects from the image
cards = [Card(img) for img in card_images]
# shuffle the card list in place
random.shuffle(cards)
   
# set each card's position on the screen
horizontal_spacing =150
vertical_spacing = 200
horizontal_indent = 750
vertical_indent = 90
marvertical_indent = 100
 
for i, card in enumerate(cards):
    pos_x = horizontal_indent + i % 5 * horizontal_spacing
    pos_y = vertical_indent + i // 5 * vertical_spacing
    card.rect.center = (pos_x, pos_y)
 
 
running = True
while running:
    mouse_pressed = False
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = True

            
   
    clock.tick(30)
   
    bg_img = pg.image.load("images/background.png")  # loads image 
    screen.blit(bg_img, (1, 1)) 
   
    # draw the cards
    for c in cards:
        c.update(mouse_pressed)
        c.draw(screen)
   
    pg.display.flip()
   
pg.quit()