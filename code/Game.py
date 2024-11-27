#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        pygame.mixer_music.load('./assets/SFX/InterStellarBattleOst.mp3')
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # Close window
            #         quit()  # End pygame
