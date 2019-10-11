import pygame

pygame.init() 
#####################################################################################
# text from here on
X = 300;
Y = 150;

font = pygame.font.Font('fonts/ARCADECLASSIC.ttf', 32) 
 
yellow = (255, 211, 0)
puntenvanplayers = (0,0,0)  
# create a text suface object, 
# on which text is drawn on it. 
player1 = font.render("Player1's points:" , True, yellow)
player2 = font.render("Player2's points:" , True, yellow)
puntentext = font.render("Punten van players :" , True, puntenvanplayers)


  
# set the center of the rectangular object. 
puntenrect = puntentext.get_rect()  
puntenrect.center = (X // 1.7,(Y - 100) // 2)

p1rect = player1.get_rect()  
p1rect.center = (X // 2, Y // 2) 

p2rect = player2.get_rect()  
p2rect.center = (X // 2, (Y + 80) // 2) 


screen.blit(player1, p1rect)
screen.blit(player2, p2rect)
screen.blit(puntentext, puntenrect)

pygame.display.flip()
