'''Imports the needed modules'''''
import pygame #imports all pygame modules
import sys #imports modules such as quit this give the user more control.


'''Initializes game'''
pygame.init() #initializes the pygame imported modules
clock = pygame.time.Clock() #to control fps/tracks time


#TODO pygame must detect current screen because it isn't
''''Detects the monitor screen and stores it in a variable'''
display_info = pygame.display.Info()


''''The menu canvas/window'''
pygame.display.set_caption("Menu") #Creates the title of the window
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h)) # Creates a canvas/window 640 * 480. Has to be used every time when using the screen
pygame.display.update() #Updates the display if this is not used, no update to the screen will come


''''Colours'''
white = (255,255,255) # The colour for the menu (White)
black = (0,0,0) # The colour for the menu (black)
screen.fill(white) # Fills the screen white (white is created as a variable without it, it wouldn't work

''''The image canvas/window'''
the_image = "D:/HR Projecten/Project Pygame/ProjectPygame/Menu images/menu.jpg"
screen_image = pygame.display.set_mode((640,480)) # Window for the image (the canvas)
menu_image =  pygame.image.load(the_image) # the image (the image that will apear on the canvas
screen_image.blit(menu_image,(0,0))


''''The font canvas/window'''
pygame.display.set_caption("Font") #creates the canves for the fonts
my_font = pygame.font.Font(None,50) # stores the fond module in my_font
menu_font = my_font.render("MENU",1,white)
start_font = my_font.render("Start",0,white)
player_font = my_font.render("Players",0,white)
highscores_font = my_font.render("High Scores",0,white)
rules_font = my_font.render("Rules", 0, white )
settings_font = my_font.render("Settings",0,white)
quit_font = my_font.render("Quit",0,white)

#imports the letters
screen.blit(menu_font,(240,10))
screen.blit(start_font,(240,90))
screen.blit(player_font,(240,160))
screen.blit(highscores_font,(240,230))
screen.blit(settings_font,(240,300))
screen.blit(rules_font, (240, 370))
screen.blit(quit_font,(240,430))


''''The menu music theme'''
pygame.mixer.music.load('musictheme.wav')
pygame.mixer.music.play()


''''The mouse'''
the_mouse_boolean = True
the_mouse_screen = pygame.display.set_mode((250,250))
pygame.display.set_caption("Pygame Mouse")





#TODO if a key is pressed go up or down in the menu
''''The loop to keep the menu open'''
run = True
while run == True: #The loop to keep the menu open, if the user clicks on the exit screen, the menu will stop.
    for events in pygame.event.get():
        if events.type == pygame.QUIT: #if the arrow is pressed, they game quits
            pygame.quit(); sys.exit()

    pygame.display.update()



