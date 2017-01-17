import pygame #imports all pygame modules
import sys #imports modules such as quit this give the user more control.


pygame.init() #initializes pygame

fps_clock = pygame.time.Clock() #to control fps/tracks time

screen = pygame.display.set_mode((640,480)) # The screen, it has to be used every time when using the screen
pygame.display.set_caption("Welcome to the menu") #Creates the title
pygame.display.update() #Updates the display if this is not used, no update to the screen will come

white = (255,255,255) # The colour for the menu (White)
while True:

