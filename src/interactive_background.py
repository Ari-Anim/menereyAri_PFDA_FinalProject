from PIL import Image
import glob
import os
import pygame



class Character_Anim():
    
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.frame = pygame.Surface([1920,1080])

        self.idle_jump_frames = []
        self.idle_frames.append(pygame.image.load("idle/start_jump.png").convert_alpha())
        self.idle_frames.append(pygame.image.load("idle/jumping.png").convert_alpha())
        self.idle_frames.append(pygame.image.load("idle/landing.png").convert_alpha())
        self.idle_frames.append(pygame.image.load("idle/move.png").convert_alpha())

        self.idle_loop_frames = []
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_1.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_2.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_3.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_4.png").convert_alpha())

        self.right_jump_frames = []
        self.right_frames.append(pygame.image.load("right/start_jump.png").convert_alpha())
        self.right_frames.append(pygame.image.load("right/jumping.png").convert_alpha())
        self.right_frames.append(pygame.image.load("right/landing.png").convert_alpha())
        self.right_frames.append(pygame.image.load("right/right_1.png").convert_alpha())

        self.right_move_frames = []
        self.right_move_frames.append(pygame.image.load("right/right_1.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_2.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_3.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_4.png").convert_alpha())

        self.left_jump_frames = []
        self.left_frames.append(pygame.image.load("left/start_jump.png").convert_alpha())
        self.left_frames.append(pygame.image.load("left/jumping.png").convert_alpha())
        self.left_frames.append(pygame.image.load("left/landing.png").convert_alpha())
        self.left_frames.append(pygame.image.load("left/left_1.png").convert_alpha())

        self.left_move_frames = []
        self.left_move_frames.append(pygame.image.load("left/left_1.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_2.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_3.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_4.png").convert_alpha())

        self.current_frame = 0
        self.frame = self.sprites[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect = self.pos

    def _detect_movement(self, mouse_click, mpos_x, mpos_y, mouse_motion, pos):
        #if mpos_y is outside window idle
        #if mpos_x is to the left side use left loop
        #if mpos_x is to the right side use right loop
        #if mouse_motion = False use idle loop.
        pass

    def _detect_jump(self, mouse_click):
        pass

    def choose_frame(self):
        pass

class foreground():
    pass


class background():
    pass


def main():
    pygame.init()
    pygame.display.set_caption("Interactive Background")
    resolution = (800, 800)
    screen = pygame.display.set_mode((resolution), pygame.RESIZABLE)
    character = pygame.sprite.Group()
    click = False
    mpos_x = 0
    mpos_y = 0
    character_pos_x = 0
    character_pos_y = 0
    mouse_motion = False
    running = True

    while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                     click = True
                if event.type == pygame.MOUSEBUTTONUP:
                     click = False
                if event.type == pygame.MOUSEMOTION:
                     mouse_motion = True
                     mpos_x, mpos_y = pygame.mouse.get_pos()
            #Render
            screen.fill((0,0,0))
            character.draw(screen)
            pygame.display.flip()
            pygame.display.flip()
    pygame.quit()
    

# TODO Load character left_
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