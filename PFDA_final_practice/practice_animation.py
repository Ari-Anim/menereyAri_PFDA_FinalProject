import pygame
import sys

class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, screen_res):
        super().__init__()
        self.screen = screen_res
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
        self.rect.topleft = [self.pos_x,self.pos_y]

    def loop(self, mpos_x, mpos_y):
        screen_x = self.screen[0]
        screen_y = self.screen[1]
        if 0 <= mpos_x <= screen_x and 0 <= screen_y <= screen_y:
            self.looping = True
        else:
             self.looping = False
    
    def end_loop(self):
        self.looping = False

    def jump(self, click):
         if click == True:
             self.is_jumping = True
    
    def detect_motion(self, mpos_x, mpos_y, screen_res):
        mouse_x = mpos_x
        mouse_y = mpos_y
        s_x = screen_res[0]
        s_y = screen_res[1]
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
        self.rect.topleft = [self.pos_x,self.pos_y]


    def update(self):
        if self.is_jumping == False and self.looping == True:
            if self.move_r == True:
                self.current_frame += 1
                self.pos_x += 60
                if self.current_frame >= len(self.frames_3):
                    self.current_frame = 0
                self.image = self.frames_3[self.current_frame]
            elif self.move_l == True:
                self.current_frame += 1
                self.pos_x -=60
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
             #self.current_frame = 0
             if self.move_r == True:
                    self.current_frame += 1
                    if self.current_frame >= len(self.frames_4):
                        self.current_frame = 0
                        self.is_jumping = False
                    self.image = self.frames_4[self.current_frame]
             elif self.move_l == True:
                    self.current_frame += 1
                    if self.current_frame >= len(self.frames_6):
                         self.current_frame = 0
                         self.is_jumping = False
                    self.image = self.frames_6[self.current_frame]
        elif self.is_jumping == True and self.looping == False:
            #self.current_frame = 0
            if self.idle == True:
                self.current_frame += 1
                if self.current_frame >= len(self.frames_2):
                    self.current_frame = 0
                    self.is_jumping = False
                self.image = self.frames_2[self.current_frame]  


    
    """def update_pos(self):
         if self.move_l == True:
              self.pos_x -= 15
         elif self.move_r == True:
              self.pos_x += 15"""




pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen_res = [screen_width,screen_height]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character_Animation")

moving_character = pygame.sprite.Group()
char_x = 250
char_y = 575
speed = 10
character = Character(char_x,char_y,screen_res)
moving_character.add(character)
mpos_x = 0
mpos_y = 0
dt = 12
click =False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mpos_x, mpos_y = event.pos
            character.detect_motion(mpos_x, mpos_y, screen_res)
            dt = 12
            character.loop(mpos_x, mpos_y)
            """character.update_pos()"""
        if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                character.jump(click)
        
        
    
    screen.fill((50,0,50))
    moving_character.draw(screen)
    moving_character.update()
    pygame.display.flip()
    clock.tick(dt)
