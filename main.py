import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

run = True
drawing = False
start = 0, 0
end = 0, 0
size = 0, 0
rect_list = []

while run:

  for ev in pygame.event.get():
    if ev.type == QUIT:
      run = False
    if ev.type == MOUSEBUTTONDOWN:
      start = ev.pos
      size = 0, 0
      drawing = True
    if ev.type == MOUSEBUTTONUP:
      end = ev.pos
      size = end[0] - start[0], end[1] - start[1]
      rect = pygame.Rect(start, size)
      rect_list.append(rect)
      drawing = False

    if ev.type == MOUSEMOTION and drawing:
      end = ev.pos
      size = end[0] - start[0], end[1] - start[1]

  screen.fill((30,30,30))
  for rect in rect_list:
    pygame.draw.rect(screen, (255, 255, 0), rect, 3)
  pygame.draw.rect(screen, (0,0,255), (start, size), 3)
  
  pygame.display.update()

pygame.exit()