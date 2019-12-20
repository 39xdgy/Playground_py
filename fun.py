import pygame


pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)

size = (700, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption("My first Game")
#BackG is DP, Background.jpeg is anime background
image = pygame.image.load("BackG.jpg")
window.blit(image, (0, 0))

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False


    #uncommon this line to make the background white
    #window.fill(White)
    pygame.draw.rect(window, Red, [55, 200, 100, 70], 0)
    pygame.draw.line(window, Green, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(window, Black, [20, 20, 250, 100], 2)

    pygame.display.flip()

    clock.tick(60)

    
pygame.quit()
