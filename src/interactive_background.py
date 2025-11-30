from PIL import Image
import glob
import os
import pygame



class Character_Frames():
    
    def __init__(self, mpos_x, mouse_motion, click, pos=(400, 800)):
        self.pos = pos
        self.click = click
        self.mpos_x = mpos_x
        self.mouse_motion = mouse_motion
        self.surface = pygame.Surface([800, 800])
        self.jump = self.detect_jump()
        self.movement = self.detect_movement()



        #re export frames to be just as large as the sprite not the size of the screen 
        #to make calculations work, otherwise the character will always be idle.
        self.idle_jump_frames = []
        self.idle_jump_frames.append(pygame.image.load("Idle/start_jump.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("Idle/jumping.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("Idle/landing.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("Idle/idle_1.png").convert_alpha())

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

        self.current_frame = 0

    def update(self):
        self.current_frame += 1
        if self.current_frame >= 4:
            self.current_frame = 0
        self.image = self._choose_loop[self.current_frame]
        self.pos = self.move_character

    def detect_movement(self):
        if self.mouse_motion == False:
            return "idle"
        elif self.mouse_motion == True and self.mpos_x < self.pos:
            return "right"
        elif self.mouse_motion == True and self.mpos_x > self.pos:
            return "left"
        else:
            return "idle"

    def detect_jump(self):
        if self.click == True:
            return "jump"

    def _choose_loop(self):
        if self.detect_movement == "idle" and self.detect_jump == False:
            return "idle_loop_frames"
        elif self.detect_movement == "idle" and self.detect_jump == True:
            return "idle_jump_frames"
        if self.detect_movement == "right" and self.detect_jump == False:
            return "right_move_frames"
        elif self.detect_movement == "right" and self.detect_jump == True:
            return "right_jump_frames"
        if self.detect_movement == "left" and self.detect_jump == False:
            return "left_move_frames"
        elif self.detect_movement == "left" and self.detect_jump == True:
            return "left_jump_frames"

    def move_character(self):
        if self.detect_movement == "right":
            self.pos[0] -= 8
            return self.pos
        elif self. detect_movement == "left":
            self.pos[0] += 8
            return self.pos
        elif self.detect_movement == "idle":
            return self.pos
        

    def draw_frame(self, surface):
        surface.blit(self.current_frame, self.pos)


class foreground():
    pass


class background():
    pass


def main():
    pygame.init()
    pygame.display.set_caption("Interactive Background")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 800)
    screen = pygame.display.set_mode((resolution), pygame.RESIZABLE)
    click = False
    mpos_x = 0
    mpos_y = 0
    mouse_motion = False
    character = Character_Frames(mpos_x, mouse_motion, click)
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
                character.update()
            #Render
            screen.fill((0,0,0))
            character.draw(screen)
            pygame.display.flip()
            dt = clock.tick(12)
    pygame.quit()
    

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