import pygame
import random

# pygame setup
pygame.init()

screen_width , screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ASTRODODGE")

player_image_original = pygame.transform.scale(pygame.image.load('./assets/astronaut.png'), (100, 100))
astroid = pygame.transform.scale(pygame.image.load('./assets/asteroid.png'), (50, 50))

player_size = player_image_original.get_size()
player_pos = [screen_width//2, screen_height - player_size[1]]
player_image = player_image_original.copy()
facing_right = False

astroid_size = astroid.get_size()
astroid_pos = [random.randint(0, screen_width-astroid_size[0]), 0]
astroid_speed = 5

clock = pygame.time.Clock()
game_over = False

speed_clock = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if speed_clock % 50 == 0:
        astroid_speed += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 10
        if facing_right:
            player_image = pygame.transform.flip(player_image, True, False)
            facing_right = False
        
    elif keys[pygame.K_RIGHT]:
        player_pos[0] += 10
        if not facing_right:
            player_image = pygame.transform.flip(player_image,True,False)
            facing_right = True

    player_pos[0] = max(0, min(player_pos[0], screen_width - player_size[0]))

    astroid_pos[1] += astroid_speed
    if astroid_pos[1] > screen_height:
        astroid_pos = [random.randint(0, screen_width-astroid_size[0]), -astroid_size[1]]

    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size[0], player_size[1])
    astroid_rect = pygame.Rect(astroid_pos[0],astroid_pos[1], astroid_size[0],astroid_size[1])

    if player_rect.colliderect(astroid_rect):
        game_over = True

    screen.fill((0,0,0))
    screen.blit(player_image, (player_pos[0], player_pos[1]))
    screen.blit(astroid, (astroid_pos[0], astroid_pos[1]))
    pygame.display.update()

    speed_clock += 1

    clock.tick(30)




pygame.quit()