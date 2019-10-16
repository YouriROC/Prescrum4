import pygame as pg
import pygame.freetype
import random

from time import sleep

 
 
def random_color():
    # return a random RGB value
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,100)
    return (r, g, b)


# init pygame
pg.init()
clock = pg.time.Clock()
 
#############################################################
#Vanaf hier Tekst / punten / clock
    
#variablen
p1punten = 0
p2punten = 0
timer = 0
yellow = (255, 211, 0)
zwart = (0,0,0) 
beurtvanplayers = ("?")

# text settings
X = 300
Y = 150

font = pg.font.Font('fonts/joystix.ttf', 20) 
  
# set text to screen
player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
puntentext = font.render("Punten van players" , True, zwart)
clockFont = font.render("Timer :" + str(timer), True, zwart)
beurt = font.render("beurt van :" , True, zwart)
beurtvanplayer = font.render(beurtvanplayers, True, yellow)
# set text coords
puntenrect = puntentext.get_rect()  
puntenrect.center = (X // 1.8,(Y - 100) // 2)

p1rect = player1.get_rect()  
p1rect.center = (X // 1.8, Y // 2) 

p2rect = player2.get_rect()  
p2rect.center = (X // 1.8, (Y + 80) // 2) 

clockrect = clockFont.get_rect()  
clockrect.center = (X // 4,(Y + 1290) // 2) 

beurtrect = beurt.get_rect()  
beurtrect.center = (X // 2,(Y + 500) // 2)

beurtvanplayerrect = beurtvanplayer.get_rect()  
beurtvanplayerrect.center = (X // 2,(Y + 550) // 2)


SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 950
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cards_flipped = []
 
# make a card class
class Card():
    def __init__(self, image, letter):
        self.frontside = image.copy()
        self.image = self.frontside
        self.rect = image.get_rect()
        self.flipped = False
        self.letter = letter
       
       
    def update(self, mouse_clicked):
        # detect the mouse position
        if mouse_clicked:
            mpos = pg.mouse.get_pos()
            if self.rect.collidepoint(mpos):
                if self.flipped == False:
                    self.flipped = True
                    global cards_flipped
                    cards_flipped.append(self)
 
        # set the card's image depending on if it is flipped or not
        if not self.flipped:
            self.image = cardback.copy()
        else:
            self.image = self.frontside
   
       
    def draw(self, screen):
        screen.blit(self.image, self.rect)


# load and store the card images
possible_cards = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
]
# create a bunch of card objects from the image
cards = []
amount_of_cards = len(possible_cards) * 2

u = 0
for i in range(0, amount_of_cards):
    if(u == amount_of_cards / 2):
        u = 0
    letter_to_load = possible_cards[u]
    
    image = None
    try:
        image = pg.image.load("images/cards/card" + letter_to_load + ".png").convert_alpha()
    except Exception as e:
        image = pg.Surface((48, 64))
        image.fill(random_color())
    
    cards.append(Card(image, letter_to_load))
    u += 1

 
# image of the card back
cardback = pg.image.load('images/cards/card_back.png')
 
# shuffle the card list in place
random.shuffle(cards)
   
# set each card's position on the screen
horizontal_spacing = 150
vertical_spacing = 200
horizontal_indent = 750
vertical_indent = 90
marvertical_indent = 100

def unflip_all_cards():
    sleep(1.30)
    global cards_flipped

    for c in cards_flipped:
        c.flipped = False

    cards_flipped = []
 
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
    screen.blit(player1, p1rect)
    screen.blit(player2, p2rect)
    screen.blit(puntentext, puntenrect)
    screen.blit(clockFont, clockrect)
    screen.blit(beurt, beurtrect)
    screen.blit(beurtvanplayer,beurtvanplayerrect)

   
    # Unflip
    if(len(cards_flipped) >= 2):
        unflip_all_cards()

    for c in cards:
        c.update(mouse_pressed)
        c.draw(screen)
   
    pg.display.flip()

pg.quit()

