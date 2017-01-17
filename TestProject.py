import pygame




pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameScreen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Test')

gameExit = False

lead_x = 300
lead_y = 300

lead_y_change = 0
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
    pygame.draw.rect(gameScreen, blue, [lead_x, lead_y,10,10])           #() <- placement of the image
    pygame.draw.rect(gameScreen, red, [300,300, 20, 20])
    pygame.display.update()

    clock.tick(120)

pygame.quit()
quit()