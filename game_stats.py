import pygame.font
import json
class GameStats():
    #track stats for alien invasion

    def __init__(self,ai_settings):
        #initialise statistics.
        self.ai_settings=ai_settings
        self.reset_stats()
        #start alien invasion in active state
        self.game_active=False

    def reset_stats(self):

        #initialise statistics that can change during the game.
        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
        with open("score.json") as file:
            a=file.read()
        self.high_score=int(a)

        
