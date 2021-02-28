import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        #create a bullet object at the ships current position.
        super(Bullet,self).__init__()
        self.screen=screen
        #create a bullet rect(0,0)and then set correct position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        #The bullet should emerge from the top of the ship,
        #so we set the top of thebullet’s rect to match the top of the ship’s rect,
        #making it look like the bullet is fired from the ship
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        #We store a decimal value for the bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        ############self.shooting=False
    def update(self):
        #Move the bullet up the screen.
        self.y-=self.speed_factor
        # Update the decimal position of the bullet.
        # Update the rect position.
        self.rect.y = self.y

    '''def update2(self,ai_settings, screen, ship ,bullets):
        if self.shooting:
            new_bullet=Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)'''

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

'''
The update() method manages the bullet’s position. When a bullet
is fired, it moves up the screen, which corresponds to a decreasing
y-coordinate value; so to update the position, we subtract the amount
stored in self.speed_factor from self.y

We then use the value of self.y
to set the value of self.rect.y. The speed_factor attribute allows us to
increase the speed of the bullets as the game progresses or as needed to
refine the game’s behavior. Once fired, a bullet’s x-coordinate value never
changes, so it will only travel vertically in a straight line.
When we want to draw a bullet, we’ll call draw_bullet(). The draw.rect()
function fills the part of the screen defined by the bullet’s rect with the
color stored in self.color.
'''
        
