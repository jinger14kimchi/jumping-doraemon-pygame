import pygame
import time
import random
from settings import *
from load_images import *
from sprites_classes import *
from texts_functions import *

pygame.init()
pygame.mixer.init()
 
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        
        pygame.draw.circle(gameDisplay, active_color, (x,y), 30)
        if click[0] == 1 and action != None:
            if action == 'Play':
                before_play()
            elif action == 'Controls':
                game_controls()
            elif action == 'Score':
                disp_score()
            elif action == 'Home':
                game_intro()
            elif action == 'Again':
                game_Loop()
            elif action == 'Quit':
                pygame.quit()
                quit()
        pygame.display.update()
    else:
        pygame.draw.circle(gameDisplay, inactive_color, (x,y) , 30)

    text_to_button(text, black, x, y, width, height)

def disp_score():
    f = open('score.txt', 'r')
    rf = f.read()
    f.close()

    disp = True
    
    while disp:   
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    disp = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(bg_image, ( 0, 0))
        
        message_to_screen('S C O R E', blue, -200, x_disp,  80, 'fonts/gg.ttf')
        message_to_screen(rf, black, 30, x_disp, 100,'fonts/gg.ttf')
   
        bY = display_height - 100
        button("Play", 100,bY,90,50, green, light_green, action = 'Play')
        button("Home", 250,bY,90,50, yellow, light_yellow,action = 'Home')
        button("Quit", 400,bY,90,50, red, light_red, action = 'Quit')
        pygame.display.update()
            
        clock.tick(fps)
        

def pause():
    paused = True
    pygame.mixer.music.pause()

    message_to_screen("Game Paused.", blue, -80, x_disp, 80)

    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE or event.type == pygame.K_RETURN:
                    paused = False

        clock.tick(fps)
    
def game_controls():
    gameCont = True
    while gameCont:   
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    gameCont = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(bg_image, ( 0, 0))
        
        message_to_screen('C O N T R O L S', blue, -200, x_disp,  80, 'fonts/gg.ttf')

        message_to_screen("The objective of this game is", black, -100,  x_disp)
        message_to_screen("to make Doraemon jump to every platforms.",black,-70,  x_disp)
        message_to_screen("Hitting the clouds or falling to the", black,  -40,  x_disp)
        message_to_screen("river will kill Doraemon.", black,  -10,  x_disp)
       
        message_to_screen("COIN: Add 5 points", black, 30, x_disp, 23,'fonts/gg.ttf')
        message_to_screen("BOMB: Deduct 1 life" , black,  60,  x_disp,  23,'fonts/gg.ttf')
        message_to_screen("SPACE: Pause the game..", black, 90,  x_disp,  23,'fonts/gg.ttf')
        message_to_screen("LEFT/RIGHT keys: Move.", black,120, x_disp,  23,'fonts/gg.ttf')
      
        bY = display_height - 100
        button("Play", 100,bY,90,50, green, light_green, action = 'Play')
        button("Score", 250,bY,90,50, yellow, light_yellow,action = 'Score')
        button("Quit", 400,bY,90,50, red, light_red, action = 'Quit')
        pygame.display.update()
        
        
def game_intro():
    intro = True

    gameDisplay.blit(bg_image, ( 0,0 ))
    while intro:      
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    intro = False

                    
            elif event.type == pygame.QUIT:
                pygame.quit()


        message_to_screen('J u m p i n g', black, -100, x_disp,  100, 'fonts/gg.ttf')
        gameDisplay.blit(doraName, (100, 300))

        bY = display_height - 120
        button("Play", 100, bY, 90, 50, green, light_green, action = 'Play')
        button("Controls", 250, bY, 90, 50, yellow, light_yellow,action = 'Controls')
        button("Quit", 400, bY,90, 50, red, light_red, action = 'Quit')
        pygame.display.update()

        clock.tick(10)

def before_play(warning=''):
    name=''
    x = display_width/2 - 50
    gameDisplay.blit(bg_image, (0, 0))
    
    message_to_screen(warning, black, 60, x_disp, 20) 
    message_to_screen('Enter your name:', black, -200, x_disp, 30)
    message_to_screen('(5 to 10 characters only)', black, -160, x_disp, 20)
    message_to_screen('Press ESC to exit.', black, 180, x_disp,  20, defaultFont)
    message_to_screen('Press ENTER to play.', black, 200, x_disp,   20, defaultFont)
    entering = True
    
    while entering:
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
                if pygame.K_a <= event.key <= pygame.K_z or event.key == pygame.K_SPACE:
                    letter = chr(event.key)
                    name += letter
                    x += 15
                    message_to_screen(letter, black, -50, x, 25)
                    
                if event.key == pygame.K_RETURN:
                    if len(name) > 8 or len(name) < 3:
                        name = ''
                        before_play('Please enter 3 to 8 characters only.')
                        
                    else:
                        entering = False
                        
    name_display(name)
                        
def name_display(name):
    message_to_screen('Hello, '+ name.capitalize(), red, 30, x_disp, 30 )
    message_to_screen('Press SPACE if you want to change name.', black, 100, x_disp, 20)

    pygame.display.update()
    display_name = True
    
    while display_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    before_play()
                if event.key == pygame.K_RETURN:
                    player_name.append(name)
                    display_name = False

    game_Loop()

                            
def game_over(running, gameOver, score):
    gameOver_sound = pygame.mixer.music.load('music/game over sound.mp3')
    pygame.mixer.music.play()

   
    
    message_to_screen("GAME OVER", red, 10, x_disp,  80, 'fonts/gg.ttf')
    message_to_screen(str(score), blue, -100, x_disp,  120, 'fonts/gg.ttf')
    
    
    save_score(score)
    
    pygame.display.update()

    while gameOver:
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    game_Loop()
                    
            elif event.type == pygame.QUIT:
                pygame.quit()

        button('Again',  100, bY, 100, 25, green, light_green, action = 'Again')
        button('Another Player',  300, bY, 100, 25, blue, light_blue, action = 'Play')
        button('Quit',  500, bY, 100, 25, red, light_red, action = 'Quit')


        pygame.display.update()


def blocks():
    p1 = Block(black, 420, 150)
    p2 = Block(black, 0, 550)
    p3 = Block(black, 320, 250)
    p4 = Block(black, 100, 350)
    p5 = Block(black, 430, 530)
    p6 = Block(black, 240, 450)
    p7 = Block(black, 100, 650)
    
    return p1,p2,p3,p4,p5, p6, p7


def save_score(score):
    print('hello')
    f = open('score.txt', 'w')
    f.write(str(score))
    f.close()

def add_coins():
    coins = FallingObjects(coin)
    return coins
    
def add_bombs():
    bombs = FallingObjects(bomb)
    return bombs

        
def game_Loop():
    bkMusic = pygame.mixer.music.load('music/Doraemon Theme Song.mp3')
    music = pygame.mixer.music.play(-1)

    score = 0
    lives = 3

    running = True
    gameOver = False
    
    # create sprites
    coins1 = add_coins()
    coins2 = add_coins()
    
    bombs = add_bombs()

    river_bound = Boundaries(river, 0, display_height-30)


    # main player sprite
    character = Player(dorae)

    # create groups of sprites
    bombGroup = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    deadly_group = pygame.sprite.Group() # river and bomb
    playerGroup = pygame.sprite.Group()
    coinsGroup = pygame.sprite.Group()


    # add sprites to their groups
    bombGroup.add(bombs)
    playerGroup.add( character )
    coinsGroup.add(coins1, coins2)
    deadly_group.add(river_bound)
    platform_group.add( blocks() )

    speed = 5

    while running:
        clock.tick(fps)

        
        if gameOver == True:
            game_over(running, gameOver, score)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
                    pygame.mixer.music.unpause()

                elif event.key == pygame.K_ESCAPE:
                    running = False

        gameDisplay.blit(bg_image, (0,0))
        
        playerGroup.update()
        coinsGroup.draw(gameDisplay)
        bombGroup.draw(gameDisplay)
        coinsGroup.update()
        bombGroup.update()
 
        player_fall = pygame.sprite.spritecollide(river_bound, playerGroup, True)
        hit_bomb = pygame.sprite.spritecollide(character, bombGroup, True)

        platform_group.update(speed)
        deadly_group.update()
        
        platform_group.draw(gameDisplay)
        deadly_group.draw(gameDisplay)
        playerGroup.draw(gameDisplay)

        hit_boundaries = pygame.sprite.spritecollide(character, deadly_group, False)
        on_platform = pygame.sprite.spritecollide(character, platform_group, False)
        hit_falling_coins = pygame.sprite.spritecollide(character, coinsGroup, True)
            
        
        if player_fall:
            gameOver = True
            
        if hit_falling_coins:
            coinsGroup.add( add_coins() )
            gameDisplay.blit(plus, (400, 550))
            score += 5
  
      
        if hit_boundaries:
            hit_bound = True
            character.pos.y = hit_boundaries[0].rect.top
            character.vel.y = 0
            message_to_screen("You're Dead", black)
            
        if on_platform:
            character.pos.y = on_platform[0].rect.top            
            character.vel.y = 0

        if not on_platform:
            score += 1 

        if hit_bomb:
            bombGroup.add( add_bombs() )
            lives -= 1

        if character.rect.y <= 75: # if hit clouds
            gameOver = True

        if lives == 0:
            gameOver = True
       
        if score % 100 == 0:
            speed += 1
            
        gameDisplay.blit(cloudy, (20, 20) )
        gameDisplay.blit(cloudy, (200, 25) )
        gameDisplay.blit(cloudy, (380, 10) )
        
        display_text(score, 'Score: ', (10,0))
        display_text(lives, 'Lives left: ', (400,0))
        display_text(player_name[-1].capitalize(), 'Player: ', (200, 0))

        # if Doraemon hits clouds
       
        pygame.display.update()


    pygame.quit()
    quit()

   
game_intro()
before_play()
game_loop()        
