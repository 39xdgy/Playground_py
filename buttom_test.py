import pygame

pygame.init()
size = (1280, 720)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Buttom test")

Open_window = True


word_for_bottom = pygame.font.SysFont('Comic Sans MS', 30)


normal_color = (200, 50, 150)
on_color = (200, 100, 150)

flag = 0


while Open_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Open_window = False

    mouse = pygame.mouse.get_pos()

    window.fill((255, 255, 255))
    
    if (mouse[0] >= 50 and mouse[0] <= 150 and mouse[1] >= 200 and mouse[1] <= 270):
        pygame.draw.rect(window, on_color, [50, 200, 100, 70], 0)
        if(pygame.mouse.get_pressed()[0]):
            print(flag)
            flag += 1
            Open_window=False

    else: 
        pygame.draw.rect(window, normal_color, [50, 200, 100, 70], 0)


    
    pygame.display.flip()

pygame.quit()
