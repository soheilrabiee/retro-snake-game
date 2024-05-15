from pygame import *
from pygame.math import Vector2
import sys, random

# Initializing pygame
init()

# Constants -> game colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# Cell and border config
cell_size = 30
number_of_cells = 25
OFFSET = 75

# Font objects
title_font = font.Font("./Graphics/ARCADECLASSIC.TTF", 60)
score_font = font.Font("./Graphics/ARCADECLASSIC.TTF", 35)


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_position(snake_body)

    def draw_food(self):
        # Food size config
        food_rect = Rect(
            OFFSET + self.position.x * cell_size,
            OFFSET + self.position.y * cell_size,
            cell_size,
            cell_size,
        )
        # Placing the food image onto the screen
        screen.blit(food_graphics, food_rect)

    # Generates random x and y cell value
    def generate_random_cell(self):
        x_pos = random.randint(0, number_of_cells - 1)
        y_pos = random.randint(0, number_of_cells - 1)
        return Vector2(x_pos, y_pos)

    # Generates random position which is not equal to snake's body position
    def generate_random_position(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position


class Snake:
    def __init__(self):
        # 3 main parts
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        # Starting direction
        self.direction = Vector2(1, 0)
        self.add_part = False

    def draw_snake(self):
        for part in self.body:
            part_rect = (
                OFFSET + part.x * cell_size,
                OFFSET + part.y * cell_size,
                cell_size,
                cell_size,
            )
            draw.rect(screen, DARK_GREEN, part_rect, 0, 7)

    def update(self):
        # Adding a new part based of direction
        self.body.insert(0, self.body[0] + self.direction)

        # Changes the add_part value if the snake eats food
        if self.add_part == True:
            self.add_part = False

        # Movement of the snake
        else:
            # Slicing the body list to remove the last part
            self.body = self.body[:-1]

    # Resets Vector2 values to defaults
    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        # State of the game
        self.is_running = True
        self.score = 0

    def draw(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def update(self):
        if self.is_running == True:
            self.snake.update()
            self.check_food_collision()
            self.check_edge_collision()
            self.check_tail_collision()

    def check_food_collision(self):
        if self.snake.body[0] == self.food.position:
            # Creates new food position on screen
            self.food.position = self.food.generate_random_position(self.snake.body)
            self.snake.add_part = True
            self.score += 1

    def check_edge_collision(self):
        # Checks snake's position with the borders of the game
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        # Resets the positions of snake and food and pauses the game
        self.snake.reset()
        self.food.position = self.food.generate_random_position(self.snake.body)
        self.is_running = False
        self.score = 0

    def check_tail_collision(self):
        # Slicing the body list to get all the parts except the head
        headless_body = self.snake.body[1:]
        # checking if the head is equal to any part of the body
        if self.snake.body[0] in headless_body:
            self.game_over()


# Creating Canvas
screen = display.set_mode(
    (2 * OFFSET + cell_size * number_of_cells, 2 * OFFSET + cell_size * number_of_cells)
)
display.set_caption("Retro Snake Game")

clock = time.Clock()

game = Game()

# Updates the snake body every 200ms
SNAKE_UPDATE = USEREVENT
time.set_timer(SNAKE_UPDATE, 200)

# loading custom food image
food_graphics = image.load("./Graphics/food.png")

# Game loop
while True:
    for events in event.get():
        if events.type == SNAKE_UPDATE:
            game.update()

        if events.type == QUIT:
            quit()
            sys.exit()

        # If any key is pressed
        if events.type == KEYDOWN:
            # Unpausing the game
            if game.is_running == False:
                game.is_running = True

            # Checking for user input to change the direction of movement
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
    # Drawing a 5px border for the game
    draw.rect(
        screen,
        DARK_GREEN,
        (
            OFFSET - 5,
            OFFSET - 5,
            cell_size * number_of_cells + 10,
            cell_size * number_of_cells + 10,
        ),
        5,
    )
    game.draw()
    # Drawing game title and score
    title_surface = title_font.render("Retro  Snake", True, DARK_GREEN)
    score_surface = score_font.render(f"Score  {game.score}", True, DARK_GREEN)
    screen.blit(title_surface, (OFFSET + 5, 20))
    screen.blit(score_surface, (OFFSET + 5, OFFSET + cell_size * number_of_cells + 10))

    # Updates the game display with every iteration
    display.update()
    # Controlling frame rate (60)
    clock.tick(60)
