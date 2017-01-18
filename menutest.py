import pygame

pygame.init()

white = (255,255,255)
black = (0, 0, 0)
red = (235,100,15)
blue = (65,105,225)

display_width = 800
display_height = 600

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("a little bit racey")


shipImg = pygame.image.load('shipIcon.png')

def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
#pygame.sprite.Sprite.add()

gameExit = False


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('backgroundBoardgame.png', [0,0])

lead_x = 300
lead_y = 300
lead_x_change = 0


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x += -30
            if event.key == pygame.K_RIGHT:
                lead_x += 30

    # lead_x += lead_x_change


    gameDisplay.fill(blue)
    gameDisplay.blit(BackGround.image, BackGround.rect)
    #pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,40,10])
    pygame.draw.ellipse(gameDisplay, white, [300, 200, 20,20])
    pygame.draw.ellipse(gameDisplay, white, [400, 200, 20,20])

    gameDisplay.fill([255, 255, 255])
    gameDisplay.blit(BackGround.image, BackGround.rect)



    ship(lead_x,lead_y)
    pygame.display.update()
    clock.tick(15)
        #print(event)






pygame.quit()
quit()



