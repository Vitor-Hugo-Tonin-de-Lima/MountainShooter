import pygame as pg
import sys

print('Setup start')
pg.init()
window = pg.display.set_mode(size=(600, 480))
print('Setup done')

print('Loop start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()  # Close window
            quit()  # End pygame

print('Loop done')
