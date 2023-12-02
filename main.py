import pygame
from constants import *
import sys

from pygame.examples.moveit import WIDTH
from pygame.examples.moveit import HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

screen.fill(BG_COLOR)

def crash():
    message_display('You Crashed')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
