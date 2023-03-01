import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((160, 120)) 
pygame.display.set_caption("PyGame lessons")
icon = pygame.image.load("./data/img/game-icon.png")
pygame.display.set_icon(icon)

bgcolor = (252, 223, 205)

walk_right = [
    pygame.image.load("./data/img/player/tile_0045.png"),
    pygame.image.load("./data/img/player/tile_0046.png")
]

ground_tile = pygame.image.load("./data/img/tile_0004.png")
ground = pygame.Surface((320, 16))
ground.blit(ground_tile, (0, 0))
ground.blit(ground_tile, (16, 0))
ground.blit(ground_tile, (32, 0))
ground.blit(ground_tile, (48, 0))
ground.blit(ground_tile, (64, 0))
ground.blit(ground_tile, (80, 0))
ground.blit(ground_tile, (96, 0))
ground.blit(ground_tile, (112, 0))
ground.blit(ground_tile, (128, 0))
ground.blit(ground_tile, (144, 0))

player_anim_count = 0
frame_count = 0
max_frame = 20

running = True
while running:

    screen.fill(bgcolor)

    screen.blit(walk_right[player_anim_count], (16, 64))
    screen.blit(ground, (0, 80))

    if frame_count % 5 == 0:
        if player_anim_count == 0:
            player_anim_count = 1
        else:
            player_anim_count = 0




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(max_frame)
    frame_count += 1