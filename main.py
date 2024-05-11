from pygame import *
from pygame.math import Vector2
import sys

# Constants -> game colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Cell config
cell_size = 30
number_of_cells = 25

# Initializing pygame
init()


class Food:
    def __init__(self):
        self.position = Vector2(5, 6)

    def draw(self):
        food_rect = Rect(
            self.position.x * cell_size,
            self.position.y * cell_size,
            cell_size,
            cell_size,
        )
        draw.rect(surface=screen, color=DARK_GREEN, rect=food_rect)


# Creating Canvas
screen = display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
display.set_caption("Retro Snake Game")
clock = time.Clock()
food = Food()

# Game loop
while True:
    for events in event.get():
        if events.type == QUIT:
            quit()
            sys.exit()

    screen.fill(GREEN)
    food.draw()

    display.update()
    # Controlling frame rate (60)
    clock.tick(60)
