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
textbox_active_color = (242, 179, 189) #Luka pink
UI_active = False
UI_text = ''
PW_active = False
PW_text = ''
PW_show_text = ''

my_ID = 'Jasonwang1575'
my_PW = 'Wjs@1997'

UIP = text_box(pygame.Rect([500, 240, 300, 30]), white, textbox_active_color)
PWP = text_box(pygame.Rect([500, 280, 300, 30]), white, textbox_active_color)


def check_login(input_ID, input_PW, right_ID, right_PW):
    if(input_ID == right_ID and input_PW == right_PW):
           print("Welcome back")
           return True
    else:
       print("Error")
       return False


def break_line(input_string):
    fin = input_string.split(', ')
    color_string = ''
    flag_for_break_line = False
    org_len = len(fin)
    start_ = 0
    end_ = 0
    for i in fin:
        #print(i)
        if i.startswith('('):
            flag_for_break_line = True
            start_ = fin.index(i)
            #print("yes!")
        if i.endswith(')'):
            flag_for_break_line = False
            color_string += i
            end_ = fin.index(i)
            fin[fin.index(i)] = color_string

            #print("Im out")
            break
        if flag_for_break_line:
            color_string += i + ', '
            #print("Change i")

    for i in range(0, end_-start_):
        del fin[start_]
    
    return fin

#log_in = False

while log_in:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log_in = False
            main_in = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if UIP.return_position().collidepoint(event.pos):
                UI_active = True
                PW_active = False
            elif PWP.return_position().collidepoint(event.pos):
                PW_active = True
                UI_active = False
            else:
                UI_active = False
                PW_active = False
        if event.type == pygame.KEYDOWN:
            if UI_active:
                if event.key == pygame.K_BACKSPACE:
                    UIP.delete_text()
                elif event.key == pygame.K_TAB:
                    PW_active = True
                    UI_active = False
                else:
                    UIP.add_text(event.unicode)
            elif PW_active:
                if event.key == pygame.K_BACKSPACE:
                    PWP.delete_text()
                    PW_show_text = PW_show_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if(check_login(UIP.return_text(), PWP.return_text(), my_ID, my_PW)):
                        log_in = False
                else:
                    PWP.add_text(event.unicode)
                    if not (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                        PW_show_text += '*'
            elif event.key == pygame.K_TAB:
                UI_active = True
                        
            
    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    
    
    if UI_active: UIP.draw_active_box(window)
    else: UIP.draw_unactive_box(window)
    if PW_active: PWP.draw_active_box(window)
    else: PWP.draw_unactive_box(window)
    
    UI_textsurface = myfont.render(UIP.return_text(), False, (0, 0, 0))
    PW_textsurface = myfont.render(PW_show_text, False, (0, 0, 0))
    window.blit(UI_textsurface, (UIP.return_position()[0]+2, UIP.return_position()[1]+4))
    window.blit(PW_textsurface, (PWP.return_position()[0]+2, PWP.return_position()[1]+4))

    if(LB.buttom_is_press(window, mouse)):
        if(check_login(UIP.return_text(), PWP.return_text(), my_ID, my_PW)):
            log_in = False
    '''
            log_in = False
            print("I'm out")
    '''

    pygame.display.flip()



create_item_buttom = buttom(pygame.Rect([1150, 580, 80, 40]), white, black)
list_buttom = buttom(pygame.Rect([1150, 630, 80, 40]), white, black)

txt_file = open("list.txt", "r")
things =  []

for line in txt_file:
    things.append(break_line(line))

print(things)

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
        print("Done!\n")
        things.append(break_line(thing.string_form()))
        print(things)
        
    pygame.display.flip()
