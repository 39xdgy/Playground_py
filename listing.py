import pygame
from item import item
from buttom import buttom
from text_box import text_box

pygame.init()

size = (1280, 720)
white = (255, 255, 255)
black = (0, 0, 0)
textbox_active_color = (242, 179, 189) #Luka pink
window = pygame.display.set_mode(size)
pygame.display.set_caption("Listing System")

log_in = True
main_in = True
start_ticks = pygame.time.get_ticks()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
LB = buttom(pygame.Rect([600, 480, 80, 40]), white, (170, 100, 230))
item_elements = ['Context', 'Level', 'State', 'Color', 'Date']
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


def add_item_window(window):
    create_window_size = (500, 600)
    create_window = pygame.display.set_mode(create_window_size)
    pygame.display.set_caption("Add item")
    is_create = True
    text_input_boxes = []
    counter = 0
    for i in item_elements:
        temp_box = text_box(pygame.Rect([110, 10 + 80*counter, 380, 70]), white, textbox_active_color)
        text_input_boxes.append(temp_box)
        counter += 1
    
    while is_create:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_create = False
        mouse = pygame.mouse.get_pos()
        pressed = pygame.key.get_pressed()
        for i in text_input_boxes:
            i.box_is_press(create_window, mouse)
            
        pygame.display.flip()
    '''
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
    '''
    temp_box = text_box(pygame.Rect([20, 20+100*(len(list_box)), 510, 80]), white, textbox_active_color)
    list_box.append(temp_box)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Listing System")















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

    UIP.write_in_box(window, myfont)
    PWP.write_in_box_with_text(window, myfont, PW_show_text)
    
    if(LB.buttom_is_press(window, mouse)):
        if(check_login(UIP.return_text(), PWP.return_text(), my_ID, my_PW)):
            log_in = False
    LB.text_in_buttom(window, myfont, "Log in")
    pygame.display.flip()


sort_buttom = buttom(pygame.Rect([1150, 530, 80, 40]), white, black)
create_item_buttom = buttom(pygame.Rect([1150, 580, 80, 40]), white, black)
list_buttom = buttom(pygame.Rect([1150, 630, 80, 40]), white, black)

txt_file = open("list.txt", "r")
things =  []

for line in txt_file:
    things.append(break_line(line))


    
list_box = []
for i in range(0,2):
    temp_box = text_box(pygame.Rect([20, 20+100*i, 510, 80]), white, textbox_active_color)
    list_box.append(temp_box)
    




    
    
while main_in:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_in = False

    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    pygame.draw.line(window, white, (550, 0), (550, 720))
    pygame.draw.line(window, white, (1100, 0), (1100, 720))

    for i in list_box:
        if(i.box_is_press(window, mouse)):
            print(i.return_position()[1])
        

    if(sort_buttom.buttom_is_press(window, mouse)):
        continue
    sort_buttom.text_in_buttom(window, myfont, "Sort")        
    if(list_buttom.buttom_is_press(window, mouse)):
        main_in = False
    list_buttom.text_in_buttom(window, myfont, "Exit")
    if(create_item_buttom.buttom_is_press(window, mouse)):
        add_item_window(window)
    create_item_buttom.text_in_buttom(window, myfont, "Add")




    pygame.display.flip()
