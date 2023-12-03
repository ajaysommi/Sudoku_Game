import pygame
from constants import *
from sudoku_generator import SudokuGenerator
import sys

pygame.init()

# Set up the main screen
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
text3 = font3.render("Easy", True, (0, 128, 0))
text4 = font3.render("Medium", True, (0, 128, 0))
text5 = font3.render("Hard", True, (0, 128, 0))

easy_rect = pygame.Rect((80, 463), (text3.get_width(), text3.get_height()))
medium_rect = pygame.Rect((250, 463), (text4.get_width(), text4.get_height()))
hard_rect = pygame.Rect((450, 463), (text5.get_width(), text5.get_height()))

screen.fill(BG_COLOR)

# Draw the title text
screen.blit(text, (WIDTH // 3 - text.get_width() // 3.3, HEIGHT // 3 - text.get_height() // 3))
screen.blit(text2, (WIDTH // 1.5 - text.get_width() // 2, HEIGHT // 1.5 - text.get_height() // 1.5))
screen.blit(text3, (80, 463))
screen.blit(text4, (250, 463))
screen.blit(text5, (450, 463))

# Update the main display
pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if easy_rect.collidepoint(event.pos):
                print("Easy mode selected")
                sudoku_screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Sudoku Board Easy")
                sudoku_screen.fill(BG_COLOR)
                for i in range(1, 9):
                    if i % 3 == 0:
                        pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, SQUARE_SIZE * i),
                                         (WIDTH, SQUARE_SIZE * i), LINE_WIDTH * 2)
                        pygame.draw.line(sudoku_screen, BLACK_COLOR, (SQUARE_SIZE * i, 0),
                                         (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH * 2)
                    else:
                        pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, SQUARE_SIZE * i),
                                         (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
                        pygame.draw.line(sudoku_screen, BLACK_COLOR, (SQUARE_SIZE * i, 0),
                                         (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
                board_obj = SudokuGenerator(9, 30)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))

                pygame.display.flip()
                pygame.time.Clock().tick(60)

            elif medium_rect.collidepoint(event.pos):
                print("Medium mode selected")
                sudoku_screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Sudoku Board Medium")
                sudoku_screen.fill(BG_COLOR)
                board_obj = SudokuGenerator(9, 40)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))

                pygame.display.flip()
                pygame.time.Clock().tick(60)
            elif hard_rect.collidepoint(event.pos):
                print("Hard mode selected")
                sudoku_screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Sudoku Board Hard")
                sudoku_screen.fill(BG_COLOR)
                board_obj = SudokuGenerator(9, 50)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))

                pygame.display.flip()
                pygame.time.Clock().tick(60)





