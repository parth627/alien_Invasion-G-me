# The pygame module contains the functionality needed to make a game.
# We’ll use the sys module to exit the game when the player quits.
import pygame
import sys
import settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from bullet import Bullet
from button import Button
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
import json
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # The line pygame.init() initializes background settings that Pygame needs to work properly. 
    screen=pygame.display.set_mode((1200,800))
    #we have used 1200,800 in game_functions.py in number_aliens_x and number_rows methods
    # here,we call pygame.display.set_mode() to create a display window called
    #screen(object), on which we’ll draw all of the game’s graphical elements.
    #The argument (1200, 800) is a tuple that defines the dimensions of the game window. 1200 wide and 800 high
    #The screen object is called a surface.
    #A surface in Pygame is a part of the screen where you display a game element.
    #When we activate the game’s animation loop,
    #this surface is automatically redrawn on every pass through the loop.   
    pygame.display.set_caption("ALIEN INVASION")
    bg_color = (230, 230, 230)
    ai_settings=settings.Settings()
    play_button=Button(ai_settings,screen,"Go")
    stats = GameStats(ai_settings)
    #We import Ship and then make an instance of Ship (named ship) after the screen has been created.
    ship=Ship(ai_settings.ship_speed_factor,screen)
    #here,we make an instance of Group and call it bullets. 
    bullets=Group()
    alien =Alien(ai_settings,screen)
    aliens=Group()
    sb=Scoreboard(ai_settings,screen,stats)
    #######################bullets2=Bullet(ai_settings,screen,ship)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # Start the main loop for the game.
    #The game is controlled by a while loop that contains an event loop and code that manages screen updates.
    # An event is an action that the user performs while playing the game,
    #such as pressing a key or moving the mouse.
    
    while True:
        # Watch for keyboard and mouse events.
        #To make our program respond to events, we’ll write an event(for)loop to
        #listen for an event and perform an appropriate task depending on the kind of event that occurred.
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                with open("score.json",'w') as file:
                    json.dump(stats.high_score,file)
                sys.exit()
                
            elif event.type==pygame.KEYDOWN:
                #Each keypress is registered as a KEYDOWN event. 
                if event.key==pygame.K_RIGHT:
                    ship.moving_right=True
                elif event.key==pygame.K_LEFT:
                    ship.moving_left=True
                elif event.key==pygame.K_SPACE:
                    # Create a new bullet and add it to the bullets group.
                    #bullets2.shooting=True
                    if len(bullets)<3:
                        new_bullet=Bullet(ai_settings, screen, ship)
                        bullets.add(new_bullet)
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    ship.moving_right=False
                elif event.key==pygame.K_LEFT:
                    ship.moving_left=False
                #elif event.key==pygame.K_SPACE:
                    #bullets2.shooting=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                gf.check_play_button(sb,ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
                

        if stats.game_active:
            ship.update()
            #next code is to remove unnecessary bullets above the screen
            for bullet in bullets.copy():
                if bullet.rect.bottom<=0:
                    bullets.remove(bullet)
                    #print(len(bullets))    #till here
            bullets.update()
            gf.update_bullet(sb,stats,ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(sb,ai_settings,stats,screen,ship,aliens,bullets)
        
        
        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        #We draw the ship onscreen by calling ship.blitme() after filling the background,
        #so the ship appears on top of the background
        ship.blitme()
        # Redraw all bullets behind ship and aliens.
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        # alien.blitme()
        aliens.draw(screen)
        # Make the most recently drawn screen visible.

        #draw the score info
        sb.show_score()
        if not stats.game_active:
            play_button.draw_button()
        pygame.display.flip()

run_game()
