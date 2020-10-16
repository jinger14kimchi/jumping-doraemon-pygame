import pygame



display_width = 600
display_height = 650

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Jumping Doraemon')


fps = 30


clock = pygame.time.Clock()
vec = pygame.math.Vector2

player_name = []
player_acc = 10
player_friction = -0.5

white = (255, 255, 255)
blue = (0, 0, 200)
light_blue = (0, 0, 255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
green = (0,200,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (255,255,0)



bY = display_height - 120
x_disp = display_width/2
             
name = ''

defaultFont = 'fonts/gg.ttf'
head_font = 'fonts/Confetti Stream.ttf'
