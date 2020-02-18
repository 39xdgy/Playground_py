import pygame
class text_box:
    
    def __init__(self, position, unactive_color, active_color):
        self.position = position
        self.UAC = unactive_color
        self.AC = active_color
        self.text = ''
    
    def change_position(self, new_position):
        self.position = new_position

    def return_position(self):
        return self.position

    def change_unactive_color(self, new_unactive_color):
        self.UAC = new_unactive_color

    def return_unactive_color(self):
        return self.UAC

    def change_active_color(self, new_active_color):
        self.AC = new_active_color

    def return_active_color(self):
        return self.AC

    def change_text(self, new_text):
        self.text = new_text

    def add_text(self, letter):
        self.text += letter

    def delete_text(self):
        self.text = self.text[:-1]
        
    def return_text(self):
        return self.text

    def draw_unactive_box(self, environment):
        pygame.draw.rect(environment, self.UAC, self.position, 0)

    def draw_active_box(self, environment):
        pygame.draw.rect(environment, self.AC, self.position, 0)

    def box_is_press(self, environment, mouse):
        if(self.return_position().collidepoint(mouse)):
            self.draw_active_box(environment)
            if(pygame.mouse.get_pressed()[0]):
                return True
        else:
            self.draw_unactive_box(environment)
        return False
