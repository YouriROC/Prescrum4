# import pygame module in this program 
import pygame 
  
# activate the pygame library 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 



display_surface = pygame.display.set_mode((X, Y )) 


# define the RGB value for white, 
#  green, blue colour . 
white = (100, 100, 100) 
green = (0, 100, 0) 
blue = (0, 0, 128) 

# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 32) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font.render('Player1', True, green, blue) 
  
# set the center of the rectangular object. 
textRect = text.get_rect()  
textRect.center = (X // 2, Y // 2) 
  
# infinite loop 
while True : 
  
    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    display_surface.blit(text, textRect)
  
        # Draws the surface object to the screen.   
    pygame.display.update()
