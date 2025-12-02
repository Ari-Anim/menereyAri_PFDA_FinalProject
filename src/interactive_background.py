from PIL import Image
import glob
import os
import pygame



class Character_Frames():
    
    def __init__(self, mpos_x, mouse_motion, click, pos=(400, 800)):
        super().__init__()
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
        self.idle_jump_frames.append(pygame.image.load("start_jump.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("jumping.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("landing.png").convert_alpha())
        self.idle_jump_frames.append(pygame.image.load("idle_1.png").convert_alpha())

        self.idle_loop_frames = []
        self.idle_loop_frames.append(pygame.image.load("idle_1.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("idle_2.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("idle_3.png").convert_alpha())
        self.idle_loop_frames.append(pygame.image.load("idle_4.png").convert_alpha())

        self.right_jump_frames = []
        self.right_jump_frames.append(pygame.image.load("right_start_jump.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right_jumping.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right_landing.png").convert_alpha())
        self.right_jump_frames.append(pygame.image.load("right_1.png").convert_alpha())

        self.right_move_frames = []
        self.right_move_frames.append(pygame.image.load("right_1.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right_2.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right_3.png").convert_alpha())
        self.right_move_frames.append(pygame.image.load("right_4.png").convert_alpha())

        self.left_jump_frames = []
        self.left_jump_frames.append(pygame.image.load("left_start_jump.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left_jumping.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left_landing.png").convert_alpha())
        self.left_jump_frames.append(pygame.image.load("left_1.png").convert_alpha())

        self.left_move_frames = []
        self.left_move_frames.append(pygame.image.load("left_1.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left_2.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left_3.png").convert_alpha())
        self.left_move_frames.append(pygame.image.load("left_4.png").convert_alpha())

        self.current_frame = 0
        anim_loops = [self.idle_loop_frames, self.idle_jump_frames, self.right_move_frames, 
                             self.right_jump_frames, self.left_move_frames, self.left_jump_frames]
        chosen_loop = self._choose_loop(anim_loops)
        chosen_frame = self.current_frame
        print(chosen_frame)
        self.image = chosen_loop[chosen_frame]


    def update(self):
        self.current_frame += 1
        if self.current_frame >= 4:
            self.current_frame = 0
        self.image = self.current_loop[self._choose_loop()[self.current_frame]]
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
        
    def _choose_loop(self, anim_loops):
        if self.detect_movement == "idle" and self.detect_jump == False:
            return anim_loops[0]
        elif self.detect_movement == "idle" and self.detect_jump == True:
            return anim_loops[1]
        if self.detect_movement == "right" and self.detect_jump == False:
            return anim_loops[2]
        elif self.detect_movement == "right" and self.detect_jump == True:
            return anim_loops[3]
        if self.detect_movement == "left" and self.detect_jump == False:
            return anim_loops[4]
        elif self.detect_movement == "left" and self.detect_jump == True:
            return anim_loops[5]

    def move_character(self):
        if self.detect_movement == "right":
            self.pos[0] -= 8
            return self.pos
        elif self.detect_movement == "left":
            self.pos[0] += 8
            return self.pos
        elif self.detect_movement == "idle":
            return self.pos
        

    def draw(self, surface):
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