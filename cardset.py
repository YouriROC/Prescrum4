import pygame as pg
import random


def random_color():
    # return a random RGB value
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,100)
    return (r, g, b)


# initialise pg
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
   
   
   
   
    #############################################################
    #Vanaf hier Tekst / punten / clock
    
#variablen
p1punten = 0
p2punten = 0
timer = 0
yellow = (255, 211, 0)
zwart = (0,0,0) 
beurtvanplayers = ("?")

#beurt player

# text from here on
X = 300;
Y = 150;

font = pg.font.Font('fonts/joystix.ttf', 20) 
  
# create a text suface object, 
# on which text is drawn on it. 
player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
puntentext = font.render("Punten van players" , True, zwart)
clock = font.render("Timer :" + str(timer), True, zwart)
beurt = font.render("beurt van :" , True, zwart)
beurtvanplayer = font.render(beurtvanplayers, True, yellow)
# set the center of the rectangular object. 
puntenrect = puntentext.get_rect()  
puntenrect.center = (X // 1.8,(Y - 100) // 2)

p1rect = player1.get_rect()  
p1rect.center = (X // 1.8, Y // 2) 

p2rect = player2.get_rect()  
p2rect.center = (X // 1.8, (Y + 80) // 2) 

clockrect = clock.get_rect()  
clockrect.center = (X // 4,(Y + 1290) // 2) 

beurtrect = beurt.get_rect()  
beurtrect.center = (X // 2,(Y + 500) // 2)

beurtvanplayerrect = beurtvanplayer.get_rect()  
beurtvanplayerrect.center = (X // 2,(Y + 550) // 2)

screen.blit(player1, p1rect)
screen.blit(player2, p2rect)
screen.blit(puntentext, puntenrect)
screen.blit(clock, clockrect)
screen.blit(beurt, beurtrect)
screen.blit(beurtvanplayer,beurtvanplayerrect)

pg.display.flip()
  
running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

#poits cointing
