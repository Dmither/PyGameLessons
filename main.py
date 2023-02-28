import pygame

# init game, set screen resolution and game name
pygame.init()
screen = pygame.display.set_mode((640, 480))  # flags=pygame.NOFRAME
pygame.display.set_caption("PyGame lessons")

# Add and set game icon
icon = pygame.image.load("./data/img/game-icon.png")
pygame.display.set_icon(icon)


# variables:
square = pygame.Surface((50, 100))
square.fill((255, 227, 92))

myFont = pygame.font.Font("./data/fonts/VT323.ttf", 30)
text_surface = myFont.render("The first game on PYGAME", True, "Red")



# set game status and main cycle
running = True
while running:

    # screen.blit(square, (100, 50))
    # pygame.draw.circle(square, "red", (0, 50), 30)

    screen.blit(text_surface, (180, 300))
    screen.blit(icon, (250, 120))




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
