from PIL import Image
import glob
import os
import pygame



class Character_Frames():
    
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.surface = pygame.Surface([800, 800])
        self.jump = self.detect_jump()
        self.movement = self.detect_movement()


        self.idle_jump_frames = []
        self.idle_jump_frames.append(pygame.image.load("idle/start_jump.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("idle/jumping.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("idle/landing.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("idle/move.png").convert_alpha())

        self.idle_loop_frames = []
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_1.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_2.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_3.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("Idle/idle_4.png").convert_alpha())

        self.right_jump_frames = []
        self.right_jump_frames.append(pygame.image.load("right/start_jump.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right/jumping.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right/landing.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right/right_1.png").convert_alpha())

        self.right_move_frames = []
        self.right_move_frames.append(pygame.image.load("right/right_1.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_2.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_3.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right/right_4.png").convert_alpha())

        self.left_jump_frames = []
        self.left_jump_frames.append(pygame.image.load("left/start_jump.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left/jumping.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left/landing.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left/left_1.png").convert_alpha())

        self.left_move_frames = []
        self.left_move_frames.append(pygame.image.load("left/left_1.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_2.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_3.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left/left_4.png").convert_alpha())

    def detect_movement(self, mpos_x, mouse_motion, pos):
        if mouse_motion == False:
            return "idle"
        elif mouse_motion == True and mpos_x < pos:
            return "right"
        elif mouse_motion == True and mpos_x > pos:
            return "left"
        else:
            return "idle"

    def detect_jump(self, click):
        if click == True:
            return "jump"

    def _choose_frame(self):
        pass

    def draw_frame(self, surface):
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