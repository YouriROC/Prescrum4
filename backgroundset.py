import pygame

#Sets custom icon
icon = pygame.image.load("images/YS.png")
pygame.display.set_icon(icon)


#Makes screen
bg_img = pygame.image.load("images/background.png")  # loads image
resolution = bg_img.get_rect().size  # gets image size
screen = pygame.display.set_mode(resolution)  # creates screen with size
pygame.display.set_caption('Memory Game')
screen.blit(bg_img, (0, 0))  # draws image to display
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

