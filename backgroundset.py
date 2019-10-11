import pygame

pygame.init() 

#Sets custom icon
icon = pygame.image.load("images/YS.png")
pygame.display.set_icon(icon)


#Makes screen
bg_img = pygame.image.load("images/background.png")  # loads image
resolution = bg_img.get_rect().size  # gets image size
screen = pygame.display.set_mode(resolution)  # creates screen with size
pygame.display.set_caption('Memory Game')
screen.blit(bg_img, (0, 0))  # draws image to display
#####################################################################################


#variablen
p1punten = 0
p2punten = 0
timer = 0
yellow = (255, 211, 0)
zwart = (0,0,0) 

# text from here on
X = 300;
Y = 150;

font = pygame.font.Font('fonts/joystix.ttf', 20) 
  
# create a text suface object, 
# on which text is drawn on it. 
player1 = font.render("Player1's points:" + str(p1punten) , True, yellow)
player2 = font.render("Player2's points:" + str(p2punten) , True, yellow)
puntentext = font.render("Punten van players" , True, zwart)
clock = font.render("Timer :" + str(timer), True, zwart)

  
# set the center of the rectangular object. 
puntenrect = puntentext.get_rect()  
puntenrect.center = (X // 1.8,(Y - 100) // 2)

p1rect = player1.get_rect()  
p1rect.center = (X // 1.8, Y // 2) 

p2rect = player2.get_rect()  
p2rect.center = (X // 1.8, (Y + 80) // 2) 

clockrect = clock.get_rect()  
clockrect.center = (X // 4,(Y + 1290) // 2) 

screen.blit(player1, p1rect)
screen.blit(player2, p2rect)
screen.blit(puntentext, puntenrect)
screen.blit(clock, clockrect)

pygame.display.flip()
  
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

