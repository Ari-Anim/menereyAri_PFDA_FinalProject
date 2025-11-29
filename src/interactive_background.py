from PIL import Image
import glob
import os
import pygame



class Character_Anim():
    
    def __init__(self, mouse_click, mpos_x, mpos_y, 
                 mouse_motion, character_pos=(0,0)):
        self.pos = character_pos
        self.frame = self.load_frames



    def load_frames(self, mouse_click, mpos_x, mpos_y):
        pass
    
    def movement(self, mouse_click, mpos_x, mpos_y, mouse_motion, pos):
        #if mpos_y is below window look down
        #if mpos_x is to the left side use left loop
        #if mpos_x is to the right side use right loop
        #if if mouse_motion = False use idle loop.
        pass



class foreground():
    pass


class background():
    pass


def main():
    pygame.init()
    pygame.display.set_caption("Interactive Background")
    resolution = (1920, 1080)
    screen = pygame.displayy.set_mode((resolution), pygame.RESIZABLE)
    click = False
    mpos_x = 0
    mpos_y = 0
    character_pos_x = 0
    character_pos_y = 0
    mouse_motion = False
    running = True

    while running:

            for event in pygame.event.get():
                if event.type == pygame.Quit:
                      running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                     click = True
                if event.type == pygame.MOUSEBUTTONUP:
                     click = False
                if event.type == pygame.MOUSEMOTION:
                     mouse_motion = True
                     mpos_x, mpos_y = pygame.mouse.get_pos()
            #Render
            pygame.display.flip()
    pygame.quit()
    

# TODO Load character frames
# TODO Organzie Frames
# TODO Implement background
# TODO Make Background Customizeable 
# TODO implement foreground
# TODO init pygame
# TODO Setup Animation Loops to be called in Game Loop.
# TODO set up conditional arguments for which character to use based on mouse input
# TODO Set up movement of character and speed





if __name__ == "__main__":
    main()