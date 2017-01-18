import pygame




pygame.init()

#below are the definitions of the colours white, black, red, green and blue you can use them by name
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,150,255)

gameScreen = pygame.display.set_mode((600,800))    #resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
pygame.display.set_caption('boardgame')                  #this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

gameExit = False

lead_x = 300                                        #important for movement of selected block
lead_y = 720

lead_y_change = 0                               #necessary for continuous movement by holding down a key
lead_x_change = 0


clock = pygame.time.Clock()


while not gameExit:                             #game loop which keeps it running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
            if event.key == pygame.K_RIGHT:
                lead_x_change = 2
            if event.key == pygame.K_UP:
                lead_y_change = -2
            if event.key == pygame.K_DOWN:
                lead_y_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0


    lead_x += lead_x_change
    lead_y += lead_y_change


    gameScreen.fill(white)

    pygame.draw.rect(gameScreen, blue, [100, 50, 400, 700])

    pygame.draw.rect(gameScreen, green, [lead_x, lead_y,10,30])           #() <- placement of the image
    pygame.draw.rect(gameScreen, green, [280,710, 10, 40])                  #also placement of the image but this one is static, hence the 280,300 <- positioned by x and y coordinates of pixel
    pygame.draw.rect(gameScreen, green, [250,700,10,50])
    pygame.draw.rect(gameScreen, green, [320,710,10,40])

    pygame.draw.rect(gameScreen, red, [320, 50, 10, 40])
    pygame.draw.rect(gameScreen, red, [420, 50, 10, 50])
    pygame.draw.rect(gameScreen, red, [360, 50, 10, 50])
    pygame.draw.rect(gameScreen, red, [210, 50, 10, 50])


    pygame.display.update()

    clock.tick(120)                                                        #frames per second (fps) counter linked to the movement in lead_x_change and lead_y_change in lines 36 to 42 (preferably change the movement for faster

pygame.quit()
quit()