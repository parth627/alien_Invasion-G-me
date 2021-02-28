"""#import pygame
import pygame.font
new_high_score=0
#from scoreboard import Scoreboard
class NHS():
    def __init__(self,ai_settings,screen,stats):
        #super(NHS,self).__init__(ai_settings,screen,stats)
        self.stats=stats
        self.new_high_score=self.stats.high_score
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.bg_color = (230, 230, 230)
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_new_high_score()
        self.fun(self,new_high_score)
        #self.sb=Scoreboard(ai_settings,screen,stats)
        
        
        
    def fun(self,new_high_score):
        self.new_high_score=new_high_score
        
    def prep_new_high_score(self):
        new_high_score=int(round(self.new_high_score,-1))
        new_high_score_str="{:,}".format(new_high_score)
        self.new_high_score_image=self.font.render(new_high_score_str,True,self.text_color,self.bg_color)
        self.new_high_score_rect=self.new_high_score_image.get_rect()
        self.new_high_score_rect.centerx=self.screen_rect.centerx
        self.new_high_score_rect.top=20
        self.screen.blit(self.new_high_score_image,self.new_high_score_rect)    
"""

import pygame
class NHS():
    def __init__(self):
        d=shelve.open('score.txt')
        stats.high_score=d['score']
        d.close()
        





























