import pygame
from random import randint


def move(press_flag, list_UDLF, move_range, x, y):
    if press_flag[list_UDLF[0]]: y -= move_range
    if press_flag[list_UDLF[1]]: y += move_range
    if press_flag[list_UDLF[2]]: x -= move_range
    if press_flag[list_UDLF[3]]: x += move_range

    if x > 1280: x = 0
    if y > 720: y = 0
    if x < 0: x = 1280
    if y < 0: y = 720
    
    return x, y


def change_score(now_score, num, font):
    str_score = 'Your Score: ' + str(now_score + num)
    return font.render(str_score, False, (255, 255, 255)), now_score + num



pygame.init()
size = (1280, 720)
window = pygame.display.set_mode(size)
pygame.display.set_caption("My first Game")
Back_image = pygame.image.load("Background.jpeg")

carryOn = True
clock = pygame.time.Clock()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
score = 0
str_score = 'Your Score: ' + str(score)
textsurface = myfont.render(str_score, False, (255, 255, 255))


star_x = randint(20, 1260)
star_y = randint(20, 700)





x = 600
y = 630

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    pressed = pygame.key.get_pressed()

    
    lis = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    x, y = move(pressed, lis, 3, x, y)

    miku_icon = pygame.image.load("miku_icon_resize.png")



    star = pygame.image.load("star_resize.png")

    if(abs(x - star_x) < 15 and abs(y - star_y) < 15):
        textsurface, score = change_score(score, 1, myfont)
        star_x = randint(20, 1260)
        star_y = randint(20, 700)
    

    
    window.blit(Back_image, (0, 0))
    window.blit(star, (star_x, star_y))
    window.blit(miku_icon, (x, y))
    window.blit(textsurface, (0, 0))
    
    pygame.display.flip()

    clock.tick(60)

    
pygame.quit()
