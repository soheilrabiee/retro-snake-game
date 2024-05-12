from pygame import *
from pygame.math import Vector2
import sys, random

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
        self.position = self.generate_random_position()

    def draw_food(self):
        food_rect = Rect(
            self.position.x * cell_size,
            self.position.y * cell_size,
            cell_size,
            cell_size,
        )
        # Placing the food image onto the screen
        screen.blit(food_graphics, food_rect)

    def generate_random_position(self):
        x_pos = random.randint(0, number_of_cells - 1)
        y_pos = random.randint(0, number_of_cells - 1)
        position = Vector2(x_pos, y_pos)
        return position


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]

    def draw_snake(self):
        for part in self.body:
            part_rect = (part.x * cell_size, part.y * cell_size, cell_size, cell_size)
            draw.rect(screen, DARK_GREEN, part_rect, 0, 7)


# Creating Canvas
screen = display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
display.set_caption("Retro Snake Game")
clock = time.Clock()
food = Food()
snake = Snake()
# loading custom food image
food_graphics = image.load("retro-snake-game/Graphics/food.png")

# Game loop
while True:
    for events in event.get():
        if events.type == QUIT:
            quit()
            sys.exit()

    screen.fill(GREEN)
    food.draw_food()
    snake.draw_snake()

    display.update()
    # Controlling frame rate (60)
    clock.tick(60)
