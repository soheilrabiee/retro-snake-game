from pygame import *
import sys

# Initializing pygame
init()

# Creating Canvas
screen = display.set_mode((750, 750))
display.set_caption("Retro Snake Game")
clock = time.Clock()

# Game loop
while True:
    for events in event.get():
        if events.type == QUIT:
            quit()
            sys.exit()

    display.update()
    # Controlling frame rate (60)
    clock.tick(60)
