# Setup
import pygame

black = (0, 0, 0)  # RGB values, ranging from 0 to 255
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Main game loop
# Everything inside this while loop happens again and again until you quit
while True:
    # Event handling
    for event in pygame.event.get():  # Check every event
        if event.type == pygame.QUIT:  # If any of them are a quit
            quit()  # Then stop the program

    # Logic
    # ...

    # Drawing
    screen.fill(black)  # Overwrite everything with a solid colour
    # Add calls to drawing functions here (e.g. pygame.draw.rect)
    pygame.display.update()
