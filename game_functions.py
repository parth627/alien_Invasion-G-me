import pygame
import sys
import settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from bullet import Bullet
import time
def get_number_aliens_x(ai_settings, alien_width):
        """Determine the number of aliens that fit in a row."""
        available_space_x = 1200 - 2 * alien_width
        number_aliens_x = int(available_space_x / (2 * alien_width))
        return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
        #determine the no of rows of aliens that fit on the screen.
        available_space_y=(800-(3*alien_height)-ship_height)
        number_rows=int(available_space_y/(2*alien_height))
        return number_rows

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
        """Create an alien and place it in the row."""
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)

def create_fleet(ai_settings, screen,ship,aliens):
        """Create a full fleet of aliens."""    
        # Create an alien and find the number of aliens in a row.
        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
        number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
        #create the fleet of aliens
        for row_number in range(number_rows):
                for alien_number in range(number_aliens_x):
                        create_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
        for alien in aliens.sprites():
                if alien.check_edges():
                        change_fleet_direction(ai_settings,aliens)
                        break
def change_fleet_direction(ai_settings,aliens):
        #drop the entire fleet and change the fleets direction.
        for alien in aliens.sprites():
                alien.rect.y+=ai_settings.fleet_drop_speed
        ai_settings.fleet_direction*=-1

def ship_hit(sb,ai_settings,stats,screen,ship,aliens,bullets):
        #respond to ship being hit by alien
        #decrement ships_left
        if stats.ship_left>0:
                stats.ship_left-=1
                sb.prep_ships()
                aliens.empty()
                bullets.empty()
                create_fleet(ai_settings,screen,ship,aliens)
                ship.center_ship()
                time.sleep(0.5)
        else:
                stats.game_active=False
                pygame.mouse.set_visible(True)


def update_aliens(sb,ai_settings,stats,screen,ship,aliens,bullets):
        #check if the fleet is at an edge
        #and then update the positions of all aliens in fleet.
        check_fleet_edges(ai_settings,aliens)
        aliens.update()
        #look for alien ship collision
        if pygame.sprite.spritecollideany(ship,aliens):
                ship_hit(sb,ai_settings,stats,screen,ship,aliens,bullets)
                #print("Ship hit!!!!")
        #look for aliens hitting the bottom of the screen
        check_aliens_bottom(sb,ai_settings,stats,screen,ship,aliens,bullets)
def update_bullet(sb,stats,ai_settings,screen,ship,aliens,bullets):
        #check for any bullets that have hit aliens
        #if so,get rid of the bullet and the alien.
        collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
        if collisions:
                for aliens in collisions.values():
                        stats.score += ai_settings.alien_points*len(aliens)
                        sb.prep_score()
                check_high_score(stats,sb)
        if len(aliens)==0:
                #destroy existing bullets and create a fleet
                #if the entire fleet is destroyed start the new level
                bullets.empty()
                #we increase the level of game
                ai_settings.increase_speed()
                stats.level+=1
                sb.prep_level()
                create_fleet(ai_settings,screen,ship,aliens)
'''
In check_bullet_alien_collisions(), any bullet that collides with an alien
becomes a key in the collisions dictionary. The value associated with each
bullet is a list of aliens it has collided with. We loop through the collisions
dictionary to make sure we award points for each alien hit:
'''

def check_aliens_bottom(sb,ai_settings,stats,screen,ship,aliens,bullets):
        #check if any aliens have reached the bottom of the screen.
        screen_rect=screen.get_rect()
        for alien in aliens.sprites():
                if alien.rect.bottom>=screen_rect.bottom:
                        #treat the same as if the ship got hit.
                        ship_hit(sb,ai_settings,stats,screen,ship,aliens,bullets)
                        break
def check_play_button(sb,ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
        """Start a new game when the player clicks Play."""
        if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
                #reset the game settings
                ai_settings.initialise_dynamic_settings()
                
                #hide the mouse cursor.
                pygame.mouse.set_visible(False)
                #reset the game stats.
                stats.reset_stats()
                stats.game_active = True

                #reset the scoreboard images
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_ships()
                #empty the list of aliens and bullets
                aliens.empty()
                bullets.empty()
                #create a new fleet and center the ship
                create_fleet(ai_settings,screen,ship,aliens)
                ship.center_ship()
'''
elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                gf.check_play_button(stats,play_button,mouse_x,mouse_y)

written in a_i.py (above code)
                print
Pygame detects a MOUSEBUTTONDOWN event when the player clicks anywhere
on the screen u, but we want to restrict our game to respond to mouse clicks
only on the Play button. To accomplish this, we use pygame.mouse.get_pos(),
which returns a tuple containing the x- and y-coordinates of the mouse
cursor when the mouse button is clicked v. We send these values to the
function check_play_button() w, which uses collidepoint() to see if the point
of the mouse click overlaps the region defined by the Play button’s rect x.
If so, we set game_active to True, and the game begins!
'''
def check_high_score(stats,sb):
        #check to see if there is a new high score.
        if stats.score>stats.high_score:
                stats.high_score=stats.score
                sb.prep_high_score()

