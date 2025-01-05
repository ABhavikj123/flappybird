import pygame
import sys
import random

pygame.init()

width, height=350, 622
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")
back_img=pygame.image.load("img_46.png")
floor_img=pygame.image.load("img_48.png")
bird_up=pygame.image.load("img_47.png")
bird_down=pygame.image.load("img_47.png")
bird_mid=pygame.image.load("img_47.png")
sound_1=pygame.mixer.Sound("airsound.mp3")
sound_2=pygame.mixer.Sound("flappy-bird-hit-sound.mp3")
sound_3=pygame.mixer.Sound("flap.mp3")
sound_4=pygame.mixer.Sound("point.mp3")
sound_5=pygame.mixer.Sound("die.mp3")
birds=[bird_up,bird_mid,bird_down]
bird_index = 0
bird_flap=pygame.USEREVENT
pygame.time.set_timer(bird_flap, 200)
bird_img=birds[bird_index]
bird_rect=bird_img.get_rect(center=(67,622//2))
bird_movement=0
gravity=0.17
floor_x = 0

pipe_img=pygame.image.load("greenpipe.png")
pipe_height=[400,350,533,490]

pipes=[]
create_pipe=pygame.USEREVENT + 1
pygame.time.set_timer(create_pipe,1200)

game_over=False
over_img=pygame.image.load("img_45.png").convert_alpha()
over_rect=over_img.get_rect(center=(width//2,height//2))



score=0
high_score=0
score_time=0
score_font=pygame.font.Font("freesansbold.ttf",27)
clock=pygame.time.Clock()

def draw_floor():
    screen.blit(floor_img,(floor_x, 520))
    screen.blit(floor_img,(floor_x + 448, 520))
    
def create_pipes():
    global score
    pipe_y=random.choice(pipe_height)  
    top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-300)) 
    bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    if score<=3:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-300)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    elif 3<score<=6:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-270)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    elif 6<score<=9:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-240)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    elif 9<score<=12:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-210)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    elif 12<score<=15:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-180)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    else:
        top_pipe=pipe_img.get_rect(midbottom=(467, pipe_y-150)) 
        bottom_pipe=pipe_img.get_rect(midtop=(467, pipe_y))
    
    return top_pipe,bottom_pipe



def pipe_animation():
    global game_over, score_time, score
    for pipe in pipes:
        if pipe.top < 0:
            flipped_pipe=pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, pipe)
        else:
            screen.blit(pipe_img, pipe)
            
        pipe.centerx -= 3
        if pipe.right < 0:
                pipes.remove(pipe)
            
        if bird_rect.colliderect(pipe):
             sound_2.play()
             sound_5.play()
             game_over=True       

def draw_score(game_state):
    if game_state == "game_on":
        
        score_text=score_font.render(str(score), True, (255, 255, 255))
        score_rect=score_text.get_rect(center=(width // 2, 66))
        screen.blit(score_text,score_rect)
        
    elif game_state=="game_over":
        score_text=score_font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect=score_text.get_rect(center=(width//2, 66))
        screen.blit(score_text, score_rect)
        
        
        high_score_text=score_font.render(f"High Score:{high_score}",True,(255, 255, 255))
        high_score_rect=high_score_text.get_rect(center=(width//2, 506))
        screen.blit(high_score_text, high_score_rect)
        
def score_update():
    global score, score_time, high_score
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                score += 1
                sound_4.play()
                score_time = False
                 
            if pipe.left <= 0:
                score_time = True
    if score > high_score:
        high_score = score
        


running=True
while running:
    clock.tick(120)
    score
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            sys.exit()
            
        if event.type==pygame.KEYDOWN:
            sound_3.play()
            sound_1.play()
            
            if event.key == pygame.K_SPACE and not game_over:
                bird_movement=0
                bird_movement=-7
            if event.key == pygame.K_SPACE and game_over:
                game_over=False
                pipes=[]
                bird_movement=0
                bird_rect=bird_img.get_rect(center=(67,622//2))
                score=0
                 
        if event.type==bird_flap:
            bird_index += 1
            
            if bird_index > 2:
                bird_index = 0

                
                bird_img=birds[bird_index]
                bird_rect=bird_up.get_rect(center=bird_rect.center)
        
        if event.type==create_pipe:

                pipes.extend(create_pipes())
        
    screen.blit(floor_img,(floor_x,550))
    
    screen.blit(back_img,(0,0))
    
    if not game_over:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        rotated_bird=pygame.transform.rotozoom(bird_img,bird_movement* -6, 1)
        if bird_rect.top<5 or bird_rect.bottom>=550:
            game_over=True
        screen.blit(rotated_bird,bird_rect)
        pipe_animation()
        score_update()
        draw_score("game_on")
    elif game_over:
        screen.blit(over_img,over_rect)
        draw_score("game_over")
        
    floor_x-=1
    if floor_x<-448:
        floor_x=0
        
    draw_floor()
    pygame.display.update()
    
pygame.quit()
sys.exit()
            
                  
            