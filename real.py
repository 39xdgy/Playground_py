import pygame
from random import randint


window_x = 1280
window_y = 720
game_start = True
start = True
score = 0
star_score = 'Your Score: ' + str(score)
score_color = (255, 255, 255)


pygame.init()
size = (window_x, window_y)

window = pygame.display.set_mode(size)
pygame.display.set_caption("The Game")
start_Background = pygame.image.load("meme_background.jpg")

start_ticks = pygame.time.get_ticks()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

text_position = myfont.render(str_score, False, score_color)

min_star = 20
star_x = randint(min_star, window_x)
star_y = randint(min_star, window_y)

start = True

game_background = pygame.image.load("Background.jpeg")

start_x = 600
start_y = 630

unclick_color = (200, 50, 150)
click_color = (200, 100, 150)

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            game_start = False

            
    window.blit(start_Background, (0, 0))

    mouse = pygame.mouse.get_pos()

    