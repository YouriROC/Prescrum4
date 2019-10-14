import pygame 

pygame.init() 
  
font = pygame.font.Font('freesansbold.ttf', 32) 
  
text = font.render('Test', False, [0, 0, 0]]) 
  
textRect = text.get_rect()  
  
textRect.center = (X // 2, Y // 2) 
  
while True : 
  
    display_surface.blit(text, textRect)
    pygame.display.update() 