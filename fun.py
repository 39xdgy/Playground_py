import pygame


pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)

size = (1280, 720)
window = pygame.display.set_mode(size)
window.fill(White)
pygame.display.set_caption("My first Game")
#BackG is DP, Background.jpeg is anime background
image = pygame.image.load("Background.jpeg")


carryOn = True

clock = pygame.time.Clock()

x = 600
y = 630

fake_x = 120
fake_y = 120

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False


    #uncommon this line to make the background white
    #window.fill(White)
    
    #pygame.draw.line(window, Green, [0, 0], [100, 100], 5)
    #pygame.draw.ellipse(window, Black, [20, 20, 250, 100], 2)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    #pygame.draw.rect(window, Red, [x, y, 55, 55], 0)
    aoligei = pygame.image.load("real_aoligei.jpeg")

    if pressed[pygame.K_w]: fake_y -= 3
    if pressed[pygame.K_s]: fake_y += 3
    if pressed[pygame.K_a]: fake_x -= 3
    if pressed[pygame.K_d]: fake_x += 3

    fake_a = pygame.image.load("aoligei.jpg")









    miku_icon = pygame.image.load("miku_icon_resize.png")



    
    window.blit(image, (0, 0))
    window.blit(miku_icon, (x, y))
    #window.blit(aoligei, (x, y))
    #window.blit(fake_a, (fake_x, fake_y))
    
    pygame.display.flip()

    clock.tick(60)

    
pygame.quit()
