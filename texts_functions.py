import pygame
from settings import *

                         
def fonts(color = black, size =  20, fontname = defaultFont):
    fontstyle = pygame.font.Font(fontname, size)
    return fontstyle                

def text_objects(text,color,size,fontname=defaultFont ):
    fontstyle = fonts(color, size, fontname)
    textSurface = fontstyle.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace =  0, x_displace = display_width/2,  size = 20, fontname = defaultFont):
    textSurf, textRect = text_objects(msg, color, size, fontname)
    textRect.center = x_displace ,(display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight):
    textSurf, textRect = text_objects(msg, color,  20)
    textRect.center = ((buttonx + buttonwidth/2), buttony + buttonheight/2)  
    gameDisplay.blit(textSurf, textRect)


def display_text(to_print, text, location):
    fontstyle = fonts(black, 25)
    display = fontstyle.render(text + str(to_print), True, black)
    gameDisplay.blit(display,(location) )
