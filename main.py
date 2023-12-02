import pygame
from constants import *
from sudoku_generator import SudokuGenerator
import sys


pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Set up fonts
number_font = pygame.font.Font(None, 400)
game_over_font = pygame.font.Font(None, 40)
font = pygame.font.SysFont(None, 72)
font2 = pygame.font.SysFont(None, 45)
font3 = pygame.font.SysFont(None, 30)
text = font.render("Welcome to Sudoku!", True, (0, 128, 0))
text2 = font2.render("Select Game Mode:", True, (0, 128, 0))
text3 = font3.render("Easy", True, (0,128,0))
text4 = font3.render("Medium", True, (0,128,0))
text5 = font3.render("Hard", True, (0,128,0))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the title text
    screen.blit(text, (WIDTH // 3 - text.get_width() // 3.3, HEIGHT // 3 - text.get_height() // 3))

    screen.blit(text2, (WIDTH // 1.5 - text.get_width() // 2, HEIGHT // 1.5 - text.get_height() // 1.5))

    screen.blit(text3, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 1.2 - text.get_height() // 1.2))

    screen.blit(text4, (WIDTH // 2 - text.get_width() // 8.3, HEIGHT // 1.2 - text.get_height() // 1.2))

    screen.blit(text5, (WIDTH // 1.2 - text.get_width() // 12, HEIGHT // 1.2 - text.get_height() // 1.2))





    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)



