from PIL import Image
import glob
import os
import pygame



class Character_Anim():
    
    def __init__(self, mouse_click, mpos_x, mpos_y, 
                 mouse_motion, character_pos=(0,0)):
        self.pos = character_pos
        self.frame = pygame.Surface([1920,1080])

        self.frames = []
        self.frames.append(pygame.image.load("idle/jumping.png"))
        self.frames.append(pygame.image.load("idle/landing.png"))
        self.frames.append(pygame.image.load("idle/mouse_down.png"))
        self.frames.append(pygame.image.load("idle/move.png"))
        self.frames.append(pygame.image.load("idle/start_jump.png"))
        self.frames.append(pygame.image.load("right/jumping.png"))
        self.frames.append(pygame.image.load("right/landing.png"))
        self.frames.append(pygame.image.load("right/mouse_down.png"))
        self.frames.append(pygame.image.load("right/move.png"))
        self.frames.append(pygame.image.load("right/start_jump.png"))
        self.frames.append(pygame.image.load("left/jumping.png"))
        self.frames.append(pygame.image.load("left/landing.png"))
        self.frames.append(pygame.image.load("left/mouse_down.png"))
        self.frames.append(pygame.image.load("left/move.png"))
        self.frames.append(pygame.image.load("left/start_jump.png"))

        self.current_frame = 0
        self.frame = self.sprites[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect = self.pos

    def _idle(self, mouse_click, mpos_x, mpos_y):
        pass

    def _right():
         pass
    
    def _left():
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
            screen.fill((200,200,0))
            Character_Anim.draw(screen)
            pygame.display.flip()
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