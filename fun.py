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
Back_image = pygame.image.load("pic/meme_background.jpg")

carryOn = True
start_ticks = pygame.time.get_ticks()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
score = 0
str_score = 'Your Score: ' + str(score)
textsurface = myfont.render(str_score, False, (255, 255, 255))


star_x = randint(20, 1260)
star_y = randint(20, 700)

start = True

miku_back_image = pygame.image.load("pic/Background.jpeg")

x = 600
y = 630


normal_color = (200, 50, 150)
on_color = (200, 100, 150)



while start:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            carryOn = False

            
    window.blit(miku_back_image, (0, 0))
    
    mouse = pygame.mouse.get_pos()

    if (mouse[0] >= 50 and mouse[0] <= 150 and mouse[1] >= 200 and mouse[1] <= 270):
        pygame.draw.rect(window, on_color, [50, 200, 100, 70], 0)
        if(pygame.mouse.get_pressed()[0]):
            start = False
            print("I'm out")
            break

    else: 
        pygame.draw.rect(window, normal_color, [50, 200, 100, 70], 0)

    pygame.display.flip()




time_string = 'Time: ' + str(score)
timesurface = myfont.render(time_string, False, (255, 255, 255))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or score == 3:
            carryOn = False
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    if(seconds == 5): 
        carryOn = False
        
    print(seconds)    
    time_string = 'Time: ' + str(seconds)
    timesurface = myfont.render(time_string, False, (255, 255, 255))

    pressed = pygame.key.get_pressed()

    
    lis = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    x, y = move(pressed, lis, 3, x, y)

    miku_icon = pygame.image.load("pic/miku_icon_resize.png")
    


    star = pygame.image.load("pic/star_resize.png")

    if(abs(x - star_x) < 15 and abs(y - star_y) < 15):
        textsurface, score = change_score(score, 1, myfont)
        star_x = randint(20, 1260)
        star_y = randint(20, 700)
    
    #if(pygame.mouse.get_pressed()[0]): print("Yeah~")

    if(score == 10):
        print("Game finished")
        print("You used", str(seconds), "to finish the game.")
        carryOn = False
    
    window.blit(Back_image, (0, 0))
    #window.fill((0, 0, 0))
    window.blit(star, (star_x, star_y))
    window.blit(miku_icon, (x, y))
    window.blit(textsurface, (0, 0))
    window.blit(timesurface, (0, 20))
    
    pygame.display.flip()


    
pygame.quit()
