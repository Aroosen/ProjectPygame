
import pygame

black = (0, 0, 0)
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
This will allow the program to load your image through this function when you call it like this:

BackGround = Background('background_image.png', [0,0])
And you will also need these two lines in your while loop:

screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)
This will fill your screen white and put the background image over it but under your other sprites and objects.
Suggestions: You should make another class for your other sprite (maybe the reason why the image is not appearing). An example could be like:

class Ship(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
You could then "activate" it like this:

ship = Ship("images\ship.png", [a, b])
Select the coordinates for a and b. You can then blit the image on to the screen like this but after your background blit statement:

screen.blit(ship.image, ship.rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    screen.fill(black)
    pygame.display.update()





