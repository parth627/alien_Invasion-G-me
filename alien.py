import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    #a class to represent a single alien in fleet

    def __init__(self,ai_settings,screen):
        #initialise the alien and set its starting pt.
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #load the alien image and set its rect attribute.
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #store the aliens exact position
        self.x=float(self.rect.x)
    def blitme(self):
        #draw the alien at its cuurent location.
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        #return true if ship hits alien.
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        #move the alien right or left.
        self.x+=(self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x=self.x

'''
Each time we update an alien’s position, we move it to the right by the
amount stored in alien_speed_factor. We track the alien’s exact position
with the self.x attribute, which can hold decimal values u. We then use
the value of self.x to update the position of the alien’s rect .


We can call the new method check_edges() on any alien to see if it’s at
the left or right edge. The alien is at the right edge if the right attribute of
its rect is greater than or equal to the right attribute of the screen’s rect.
It’s at the left edge if its left value is less than or equal to 0.
We modify the method update() to allow motion to the left or right 
by multiplying the alien’s speed factor by the value of fleet_direction. If
fleet_direction is 1, the value of alien_speed_factor will be added to the
alien’s current position, moving the alien to the right; if fleet_direction
is −1, the value will be subtracted from the alien’s position, moving the
alien to the left.
'''

    
        
        
    
