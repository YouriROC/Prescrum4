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
# Variables
p1punten = 0
p2punten = 0
ptotalpunten = 0
timer = 0
flipsounds = 0
yellow = (87, 80, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
zwart = (0,0,0) 
beurtvanplayers = "Player1"

# text settings
X = 300
Y = 150

font = pg.font.Font('fonts/joystix.ttf', 20)
winfont = pg.font.Font('fonts/joystix.ttf', 40) 
  
# cardflip audio
flipSound1 = pg.mixer.Sound("audio/cardflip1.wav")
flipSound2 = pg.mixer.Sound("audio/cardflip2.wav")
flipSound3 = pg.mixer.Sound("audio/cardflip3.wav")
flipSound4 = pg.mixer.Sound("audio/cardflip4.wav")
flipSound5 = pg.mixer.Sound("audio/cardflip5.wav")
flipSound6 = pg.mixer.Sound("audio/cardflip6.wav")
flipSound7 = pg.mixer.Sound("audio/cardflip7.wav")
flipSound8 = pg.mixer.Sound("audio/cardflip8.wav")

# set text to screen
player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
puntentext = font.render("Punten van players" , True, zwart)
#clockFont = font.render("Timer :" + str(timer), True, zwart)
beurt = font.render("beurt van :" , True, zwart)
beurtvanplayer = font.render(beurtvanplayers, True, blue)
# set text coords
puntenrect = puntentext.get_rect()  
puntenrect.center = (X // 1.8, Y // 2)

p1rect = player1.get_rect()  
p1rect.center = (X // 1.8, (Y + 100) // 2) 

p2rect = player2.get_rect()  
p2rect.center = (X // 1.8, (Y + 150) // 2) 

#clockrect = clockFont.get_rect()  
#clockrect.center = (X // 4,(Y + 1290) // 2) 

beurtrect = beurt.get_rect()  
beurtrect.center = (X // 2,(Y + 500) // 2)

beurtvanplayerrect = beurtvanplayer.get_rect()  
beurtvanplayerrect.center = (X // 2,(Y + 550) // 2)


SCREEN_WIDTH = 1450
SCREEN_HEIGHT = 950
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

cards_flipped = []
 
# random flipsounds
def flipsound():
    flipsounds = random.randint(0, 7)
    if flipsounds == 0:
        flipSound1.play()
    if flipsounds == 1:
        flipSound2.play()
    if flipsounds == 2:
        flipSound3.play()
    if flipsounds == 3:
        flipSound4.play()
    if flipsounds == 4:
        flipSound5.play()
    if flipsounds == 5:
        flipSound6.play()
    if flipsounds == 6:
        flipSound7.play()
    if flipsounds == 7:
        flipSound8.play()


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
                    global flipSound1
                    flipsound()
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
#random.shuffle(cards)
   
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
    screen.fill(zwart)
   
    bg_img = pg.image.load("images/background.png")  # loads image

    screen.blit(bg_img, (1, 1)) 
    screen.blit(player1, p1rect)
    screen.blit(player2, p2rect)
    screen.blit(puntentext, puntenrect)
    #screen.blit(clockFont, clockrect)
    screen.blit(beurt, beurtrect)
    screen.blit(beurtvanplayer, beurtvanplayerrect)

        
    # Change turns p1 and p2
    def p1_add_point():
        global p1punten
        global ptotalpunten
        global player1
        global player2
        global beurtvanplayer
        p1punten += 1
        ptotalpunten += 1
        player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
        player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
        beurtvanplayer = font.render(beurtvanplayers, True, blue)
        sleep(0.50)

    def p2_add_point():
        global p2punten
        global ptotalpunten
        global player1
        global player2
        global beurtvanplayer
        p2punten += 1
        ptotalpunten += 1
        player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
        player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
        beurtvanplayer = font.render(beurtvanplayers, True, red)
        sleep(0.50)
        
            


    # Unflip
    if(len(cards_flipped) >= 2):
        if(cards_flipped[0].letter == cards_flipped[1].letter):
            cards.remove(cards_flipped[0])
            cards.remove(cards_flipped[1])

            if beurtvanplayers == "Player1":
                p1_add_point()
            elif beurtvanplayers == "Player2":
                p2_add_point()

            #MAKE POINTS 
            unflip_all_cards()
        else:
            if beurtvanplayers == "Player1":
                beurtvanplayers = "Player2"
                beurtvanplayer = font.render(beurtvanplayers, True, red)
            elif beurtvanplayers == "Player2":
                beurtvanplayers = "Player1"
                beurtvanplayer = font.render(beurtvanplayers, True, blue)
            unflip_all_cards()
    
    if ptotalpunten >= 10:
        if p1punten == p2punten:
                win_img = pg.image.load("images/winscreen.png")
                screen.blit(win_img, (1, 1))

                tiewinner = winfont.render("Gelijkspel!", True, yellow)
                tiewinnerrect = tiewinner.get_rect()  
                tiewinnerrect.center = (X // 100, (Y + 45) // 50)
                screen.blit(tiewinner, (520, 475))


        elif p1punten >= p2punten:
            win_img = pg.image.load("images/winscreen.png")
            screen.blit(win_img, (1, 1))

            p1winner = winfont.render("Player 1 heeft gewonnen!", True, blue)
            p1winnerrect = p1winner.get_rect()  
            p1winnerrect.center = (X // 100, (Y + 45) // 50)
            screen.blit(p1winner, (400, 475))

        elif p2punten >= p1punten:
            win_img = pg.image.load("images/winscreen.png")
            screen.blit(win_img, (1, 1))

            p2winner = winfont.render("Player 2 heeft gewonnen!", True, red)
            p2winnerrect = p2winner.get_rect()  
            p2winnerrect.center = (X // 100, (Y + 45) // 50)
            screen.blit(p2winner, (400, 475))

        fireworks = [pg.image.load('images/FW1.png'), pg.image.load('images/FW2.png'), pg.image.load('images/FW3.png'), pg.image.load('images/FW4.png'), pg.image.load('images/FW5.png'), pg.image.load('images/FW6.png'), pg.image.load('images/FW7.png'), pg.image.load('images/FW8.png')]

    

    

    for c in cards:
        c.update(mouse_pressed)
        c.draw(screen)
   
    pg.display.flip()

pg.quit()