"GenAI project"

import pygame
import random

WIDTH  = 900
HEIGHT = 900
FPS    = 30

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyTask")
clock = pygame.time.Clock()

running = True

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()