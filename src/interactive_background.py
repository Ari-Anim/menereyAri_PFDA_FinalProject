import pygame
import sys
import random

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
        self.current_jump_frame = 0
        self.image = self.frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x,self.pos_y]

    def loop(self, mpos_x, mpos_y):
        screen_x = self.screen[0]
        screen_y = self.screen[1]
        if 0 <= mpos_x <= screen_x and 0 <= mpos_y <= screen_y:
            self.looping = True
        else:
             self.looping = False
    
    def end_loop(self):
        self.looping = False
        self.move_l = False
        self.move_r = False
        self.idle = True
        self.is_jumping = False

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



    def update(self, speed):
        s_x = self.screen[0]
        s_y = self.screen[1]
        if self.is_jumping == False and self.looping == True:
            if self.move_r == True:
                self.current_frame += 1
                self.pos_x += speed
                if self.current_frame >= len(self.frames_3):
                    self.current_frame = 0
                self.image = self.frames_3[self.current_frame]
            elif self.move_l == True:
                self.current_frame += 1
                self.pos_x -=speed
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
                    self.current_jump_frame += 1
                    self.pos_x += speed*2.5
                    if self.current_jump_frame == 1:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 2:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 3:
                        self.pos_y = s_y - 150
                    if self.current_jump_frame >= len(self.frames_4):
                        self.current_jump_frame = 0
                        self.is_jumping = False
                    self.image = self.frames_4[self.current_jump_frame]
             elif self.move_l == True:
                    self.pos_x -= speed*2.5
                    self.current_jump_frame += 1
                    if self.current_jump_frame == 1:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 2:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 3:
                        self.pos_y = s_y - 150
                    if self.current_jump_frame >= len(self.frames_6):
                         self.current_jump_frame = 0
                         self.is_jumping = False
                    self.image = self.frames_6[self.current_jump_frame]
        elif self.is_jumping == True and self.looping == False: 
                if self.idle == True:
                    self.current_jump_frame += 1
                    if self.current_jump_frame == 1:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 2:
                        self.pos_y = s_y - 200
                    if self.current_jump_frame == 3:
                        self.pos_y = s_y - 150
                    if self.current_jump_frame >= len(self.frames_2):
                        self.current_jump_frame = 0
                        self.is_jumping = False
                    self.image = self.frames_2[self.current_jump_frame]  
        self.rect.topleft = [self.pos_x,self.pos_y]
        if self.rect.left < 0:
            self.rect.left = 0
            self.move_l = False
            self.looping = False
            self.idle = True
        if self.rect.right > 1200:
            self.rect.left = 1100
            self.move_r = False
            self.looping = False
            self.idle = True

    def get_rect(self):
        character_rect = self.rect
        return character_rect



class Obstacles(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, screen_res):
        self.screen = screen_res
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coords = (self.pos_x, self.pos_y)
        self.looping = False
        self.alpha = 255

        self.speed = 5
        self.obstacle_frames = []
        self.obstacle_frames.append(pygame.image.load('obstacle_1.png'))
        self.obstacle_frames.append(pygame.image.load('obstacle_2.png'))
        self.obstacle_frames.append(pygame.image.load('obstacle_3.png'))
        self.obstacle_frames.append(pygame.image.load('obstacle_4.png'))

        self.current_frame = 0
        self.image = self.obstacle_frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.rect_0 = self.rect[2]
        self.rect_1 = self.rect[3]


    def check_looping(self, running):
        if running == True:
            self.looping = True


    def update(self):
        if self.looping == True:
            self.current_frame += 1
            if self.current_frame >= len(self.obstacle_frames):
                self.current_frame = 0
            self.pos_x += self.speed
            if self.pos_x >= 900:
                self.pos_x = -100
            self.coords = (self.pos_x, self.pos_y)
            self.image = self.obstacle_frames[self.current_frame]

    
    def draw(self, surface):
        if self.looping == True:
            surface.blit(self.image,self.coords)
    
    def get_new_rect(self):
        obstacle_rect = self.image.get_rect()
        return obstacle_rect
    
    def is_colliding(self, colliding):
        pass




class Grass():
    def __init__(self):
        self.grass_pos_y = 600
        self.grass_pos_x = -1200

        self.grass = []
        self.grass.append(pygame.image.load('grass1.png'))
        self.grass.append(pygame.image.load('grass2.png'))
        self.grass.append(pygame.image.load('grass3.png'))
        self.grass.append(pygame.image.load('grass4.png'))
        self.grass.append(pygame.image.load('grass5.png'))
        self.grass.append(pygame.image.load('grass6.png'))
        self.grass.append(pygame.image.load('grass7.png'))
        self.grass.append(pygame.image.load('grass8.png'))

        self.current_frame = 0
        self.image = self.grass[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.grass_pos_x,self.grass_pos_y]


    def update(self):
        self.current_frame += 1
        if self.current_frame >= len(self.grass):
            self.current_frame = 0
        self.image = self.grass[self.current_frame]
    
    def draw(self, screeen):
        surface = screen
        if self.current_frame == 0:
            surface.blit(self.grass[0], (0,self.grass_pos_y))
        if self.current_frame == 1:
            surface.blit(self.grass[1], (0,self.grass_pos_y))
        if self.current_frame == 2:
            surface.blit(self.grass[2], (0,self.grass_pos_y))
        if self.current_frame == 3:
            surface.blit(self.grass[3], (0,self.grass_pos_y))
        if self.current_frame == 4:
            surface.blit(self.grass[4], (0,self.grass_pos_y))
        if self.current_frame == 5:
            surface.blit(self.grass[5], (0,self.grass_pos_y))   
        if self.current_frame == 6:
            surface.blit(self.grass[6], (0,self.grass_pos_y))
        if self.current_frame == 7:
            surface.blit(self.grass[7], (0,self.grass_pos_y))



class Background():
    def __init__(self, dt, screen_res):
        self.dt = dt
        self.screen = screen_res
        self.img_path = "bkg.png"
        self.img_path_2 = "floor.png"
        self.img_path_3 = "clouds.png"
        self.image_bkg = pygame.image.load(self.img_path).convert_alpha()
        self.image_floor = pygame.image.load(self.img_path_2).convert_alpha()
        self.image_clouds = pygame.image.load(self.img_path_3).convert_alpha()
        self.cloud_pos_x = -800



    def update(self):
        self.cloud_pos_x += 10
        if self.cloud_pos_x >= 1800:
            self.cloud_pos_x = -2400


    def draw(self, screen):
        screen.blit(self.image_bkg, (0,0))
        screen.blit(self.image_clouds,(self.cloud_pos_x, 150))
        screen.blit(self.image_floor,(0, 750))



class Fog():
    def __init__(self):
        self.img_path = "clouds2.png"
        self.image_fog = pygame.image.load(self.img_path).convert_alpha()
        self.fog_x = -2400
        self.fog_y = 600

        self.rect = self.image_fog.get_rect()
        self.rect.topleft = [self.fog_x,self.fog_y]

    def update(self):
        self.fog_x += 60
        if self.fog_x >= 1200:
            self.fog_x = -2400

    def draw(self):
        screen.blit(self.image_fog,(self.fog_x, self.fog_y))



pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 800
screen_res = [screen_width,screen_height]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character_Animation")
moving_character = pygame.sprite.Group()
char_x = screen_width//2 - 150
char_y = screen_height - 150
speed = 30
character = Character(char_x,char_y,screen_res)
obst_x = screen_width//2 - 300
obst_y = screen_height - 150
obstacle = Obstacles(obst_x, obst_y, screen_res)
moving_character.add(character)
mpos_x = 0
mpos_y = 0
red = 50
green = 0
blue = 50
alpha = 50
dt = 12
background = Background(dt, screen_res)
grass = Grass()
fog = Fog()
click =False
mouse_motion = False
running = True
colliding = False
char_rect = character.get_rect()
obs_rect = obstacle
points_counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mpos_x, mpos_y = event.pos
            mouse_motion = True
            character.detect_motion(mpos_x, mpos_y, screen_res)
            dt = 12
            character.loop(mpos_x, mpos_y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                character.jump(click)
                #bkg.update(click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                character.end_loop()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                red += 50
                blue += 50
        obstacle.check_looping(running)
    #collision

    if char_rect.colliderect(obs_rect) == True:
        colliding = True
    if colliding == True:
        obstacle.image.set_alpha(0)
    if obstacle.pos_x == -100:
        colliding = False
        if obstacle.image.get_alpha() == 0:
            obstacle.image.set_alpha(255)
    
    print(obstacle.pos_x)
    #light
    """if red > 70:
        red -= 5
    elif 70 >= red > 50:
        red -= 10
    if blue > 70:
        blue -= 5
    elif 70 >= blue > 50:
        blue -= 10"""
    
    screen.fill((red,green,blue))
    background.update()
    background.draw(screen)
    grass.update()
    grass.draw(screen)
    fog.update()
    fog.draw()
    moving_character.draw(screen)
    moving_character.update(speed)
    obstacle.draw(screen)
    obstacle.update()
    pygame.display.flip()
    clock.tick(12)

    
# TODO Make Background Customizeable 




if __name__ == "__main__":
    main()