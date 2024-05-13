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
        # Food size config
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
        # 3 main parts
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        # Starting direction
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for part in self.body:
            part_rect = (part.x * cell_size, part.y * cell_size, cell_size, cell_size)
            draw.rect(screen, DARK_GREEN, part_rect, 0, 7)

    def update(self):
        # Slicing the body list to remove the last part
        self.body = self.body[:-1]
        # Adding new part based of direction
        self.body.insert(0, self.body[0] + self.direction)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def draw(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def update(self):
        self.snake.update()


# Creating Canvas
screen = display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))
display.set_caption("Retro Snake Game")

clock = time.Clock()

game = Game()

# Updates the snake body every 200ms
SNAKE_UPDATE = USEREVENT
time.set_timer(SNAKE_UPDATE, 200)

# loading custom food image
food_graphics = image.load("retro-snake-game/Graphics/food.png")

# Game loop
while True:
    for events in event.get():
        if events.type == SNAKE_UPDATE:
            game.update()

        if events.type == QUIT:
            quit()
            sys.exit()

        # Checking for user input to change the direction of movement
        if events.type == KEYDOWN:
            if events.key == K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if events.key == K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if events.key == K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if events.key == K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)

    # Drawing on screen
    screen.fill(GREEN)
    game.draw()

    display.update()
    # Controlling frame rate (60)
    clock.tick(60)
