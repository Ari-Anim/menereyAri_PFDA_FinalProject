import pygame
import sys

class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.frames = []
        self.frames_2 = []
        self.frames_3 = []
        self.frames_4 = []
        self.frames_5 = []
        self.frames_6 = []
        self.looping = False
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_l = False
        self.move_r = False
        self.idle = True
        self.is_jumping = False

        self.frames.append(pygame.image.load('idle_1.png'))
        self.frames.append(pygame.image.load('idle_2.png'))
        self.frames.append(pygame.image.load('idle_3.png'))
        self.frames.append(pygame.image.load('idle_4.png'))
        self.frames_2.append(pygame.image.load('idle_1.png'))
        self.frames_2.append(pygame.image.load('idle_start_jump.png'))
        self.frames_2.append(pygame.image.load('idle_jump.png'))
        self.frames_2.append(pygame.image.load('idle_landing.png'))
        self.frames_3.append(pygame.image.load('right_1.png'))
        self.frames_3.append(pygame.image.load('right_2.png'))
        self.frames_3.append(pygame.image.load('right_3.png'))
        self.frames_3.append(pygame.image.load('right_4.png'))
        self.frames_4.append(pygame.image.load('right_1.png'))
        self.frames_4.append(pygame.image.load('right_start_jump.png'))
        self.frames_4.append(pygame.image.load('right_jumping.png'))
        self.frames_4.append(pygame.image.load('right_landing.png'))
        self.frames_5.append(pygame.image.load('left_1.png'))
        self.frames_5.append(pygame.image.load('left_2.png'))
        self.frames_5.append(pygame.image.load('left_3.png'))
        self.frames_5.append(pygame.image.load('left_4.png'))
        self.frames_6.append(pygame.image.load('left_1.png'))
        self.frames_6.append(pygame.image.load('left_start_jump.png'))
        self.frames_6.append(pygame.image.load('left_jumping.png'))
        self.frames_6.append(pygame.image.load('left_landing.png'))

        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def loop(self):
         self.looping = True
    
    def end_loop(self):
        self.looping = False

    def jump(self, click):
         self.is_jumping = True
    
    def detect_motion(self, mpos_x, mpos_y, screen_size):
        mouse_x = mpos_x
        mouse_y = mpos_y
        s_x = screen_size[0]
        s_y = screen_size[1]
        if self.is_jumping == True:
            if mpos_x > s_x or mpos_x < 0:
                self.move_l = False
                self.move_r = False
                self.idle = True
            elif mpos_y > s_y or mpos_y > 0:
                self.idle = True
                self.move_l = False
                self.move_r = False
            elif self.pos_x > mouse_x:
                self.move_l = True
                self.move_r = False
                self.idle = False
            elif self.pos_x < mouse_x:
                self.move_r = True
                self.move_l = False
                self.idle = False
        elif self.is_jumping == False:
            if mpos_x > s_x or mpos_x < 0:
                self.move_l = False
                self.move_r = False
                self.idle = True
            elif self.pos_x > mouse_x:
                self.move_l = True
                self.move_r = False
                self.idle = False
            elif self.pos_x < mouse_x:
                self.move_r = True
                self.move_l = False
                self.idle = False


    def update(self):
        if self.is_jumping == False and self.looping == True:
            if self.move_r == True:
                self.current_frame += 1
                if self.current_frame >= len(self.frames_3):
                    self.current_frame = 0
                self.image = self.frames_3[self.current_frame]
            elif self.move_l == True:
                self.current_frame += 1
                if self.current_frame >= len(self.frames_5):
                    self.current_frame = 0
                self.image = self.frames_5[self.current_frame]
        elif self.looping == False and self.is_jumping == False:
                self.idle = True
                self.move_l = False
                self.move_r = False
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0
                self.image = self.frames[self.current_frame]
        elif self.is_jumping == True and self.looping == True:
             if self.move_r == True:
                    self.current_frame += 1
                    if self.current_frame >= len(self.frames_4):
                         self.current_frame = 0
                    self.image = self.frames_4[self.current_frame]

    
    def update_right(self):
        pass

    def update_left(self):
        pass
    
    def jump(self):
        pass



pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen_size = [screen_width,screen_height]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character_Animation")

moving_character = pygame.sprite.Group()
character = Character(250,575)
moving_character.add(character)
mpos_x = 0
mpos_y = 0
dt = 12

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
                mpos_x, mpos_y = event.pos
                character.detect_motion(mpos_x, mpos_y, screen_size)
        if event.type == pygame.MOUSEBUTTONDOWN:
                dt = 12
                character.loop()
        if event.type == pygame.MOUSEBUTTONUP:
                dt = 6
                character.end_loop()
        
    
    screen.fill((0,0,0))
    moving_character.draw(screen)
    moving_character.update()
    pygame.display.flip()
    clock.tick(dt)
