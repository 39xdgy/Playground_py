import pygame
from item import item
from buttom import buttom
from text_box import text_box

pygame.init()

size = (1280, 720)
white = (255, 255, 255)
black = (0, 0, 0)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Listing System")

log_in = True
main_in = True
start_ticks = pygame.time.get_ticks()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
LB = buttom(pygame.Rect([600, 480, 80, 40]), white, (170, 100, 230))
UIP = pygame.Rect([500, 240, 300, 30])
PWP = pygame.Rect([500, 280, 300, 30])
textbox_active_color = (242, 179, 189) #Luka pink
UI_active = False
UI_text = ''
PW_active = False
PW_text = ''
PW_show_text = ''

my_ID = 'Jasonwang1575'
my_PW = 'Wjs@1997'




def check_login(input_ID, input_PW, right_ID, right_PW):
    if(input_ID == right_ID and input_PW == right_PW):
           print("Welcome back")
           return True
    else:
       print("Error")
       return False
            



while log_in:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log_in = False
            main_in = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if UIP.collidepoint(event.pos):
                UI_active = True
                PW_active = False
            elif PWP.collidepoint(event.pos):
                PW_active = True
                UI_active = False
            else:
                UI_active = False
                PW_active = False
        if event.type == pygame.KEYDOWN:
            if UI_active:
                if event.key == pygame.K_BACKSPACE:
                    UI_text = UI_text[:-1]
                elif event.key == pygame.K_TAB:
                    PW_active = True
                    UI_active = False
                else:
                    UI_text += event.unicode
            elif PW_active:
                if event.key == pygame.K_BACKSPACE:
                    PW_text = PW_text[:-1]
                    PW_show_text = PW_show_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if(check_login(UI_text, PW_text, my_ID, my_PW)):
                        log_in = False
                else:
                    PW_text += event.unicode
                    if not (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                        PW_show_text += '*'
            elif event.key == pygame.K_TAB:
                UI_active = True
                        
            
    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    if UI_active:
        pygame.draw.rect(window, textbox_active_color, UIP, 0)
    else:
        pygame.draw.rect(window, white, UIP, 0)
    if PW_active:
        pygame.draw.rect(window, textbox_active_color, PWP, 0)
    else:
        pygame.draw.rect(window, white, PWP, 0)
    
    UI_textsurface = myfont.render(UI_text, False, (0, 0, 0))
    PW_textsurface = myfont.render(PW_show_text, False, (0, 0, 0))
    window.blit(UI_textsurface, (UIP[0]+2, UIP[1]+4))
    window.blit(PW_textsurface, (PWP[0]+2, PWP[1]+4))

    if(LB.buttom_is_press(window, mouse)):
        if(check_login(UI_text, PW_text, my_ID, my_PW)):
            log_in = False
    '''
            log_in = False
            print("I'm out")
    '''

    pygame.display.flip()



create_item_buttom = buttom(pygame.Rect([1150, 580, 80, 40]), white, black)
list_buttom = buttom(pygame.Rect([1150, 630, 80, 40]), white, black)

while main_in:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_in = False

    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    pygame.draw.line(window, white, (550, 0), (550, 720))
    pygame.draw.line(window, white, (1100, 0), (1100, 720))
    
    if(list_buttom.buttom_is_press(window, mouse)):
        main_in = False

    if(create_item_buttom.buttom_is_press(window, mouse)):
        context = str(input("context: "))
        level = int(input("level: "))
        state = int(input("State: "))
        color = str(input("color: "))
        date = str(input("date: "))
        thing = item(context, level, state, color, date)
        thing.write_file("list.txt")
        print("Done!")
        
    pygame.display.flip()
