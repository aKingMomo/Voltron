import pygame
import math
import random

#color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)
CYAN = (0,255,255)

enemy_speed = 5




#character is name of player sprite, either Castle, Red, Green, Blue, Yellow or Black
#TODO when adding to renpy: Select character based on points
character = "Castle"



class Enemy(pygame.sprite.Sprite):
    def __init__(self,xtarget,ytarget):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("Galra.png").convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.xpos = 0.0
            self.ypos = 0.0
            self.xspeed = enemy_speed
            self.yspeed = 0
            #new movement code - takes the coordinates of the player sprite, and sets enemy initial velocity towards the player
            #for this, xpos (initial x) is set to a random float between 0.0 and 1000.0 and ypos (initial y) is 0.0
            #self.rect.x and y are set to x and y pos in the init loop
            """if abs(xtarget - self.xpos) >=50:
            	self.yspeed = -enemy_speed * (self.ypos - ytarget)/abs(self.xpos - xtarget)
            	self.xspeed = -enemy_speed * (self.xpos - xtarget)/abs(self.ypos - ytarget)
            else:
            	self.yspeed = enemy_speed
            	self.xspeed = 0"""
            self.health = 1


    #updates position of enemy, returns True if past edge of screen
    def update(self):
       #check if past boundary (will be destroyed)
        
        if self.rect.x >= 1300 or self.rect.y>=800:
            return True
        
        #old movement code
        else:
            
            if self.rect.x == 1150: 
                self.xspeed = 0
                self.yspeed = enemy_speed
            if self.rect.y == 160:
                self.xspeed = -enemy_speed
                self.yspeed = 0
            if self.rect.x == 10:
                self.xspeed = 0
                self.yspeed = enemy_speed
            if self.rect.y == 300:
                self.xspeed = enemy_speed
                self.yspeed = 0

            self.rect.x += self.xspeed
            self.rect.y += self.yspeed
            return False

    #called when hit by projectile, returns true if to be destroyed
    def collide(self):
            self.health -= 1
            if self.health == 0:
                return True
            else:
                return False



class Projectile(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10,30])
            self.image.fill(CYAN)
            self.rect = self.image.get_rect()
            self.yspeed = -10

    #update the projectile position, returns true if it has passed the top of the screen
    def update(self):
            if self.rect.y <= -self.rect.y:
                return True
            else:
                self.rect.y += self.yspeed
                return False

    
class Player(pygame.sprite.Sprite):
    def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load("%s.png" %(character)).convert()
			self.image.set_colorkey(BLACK)
			self.rect = self.image.get_rect()
			self.health =3
		
			

        
def main():
    pygame.init()

    size = (1280,720)
    screen = pygame.display.set_mode(size)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    background_image = pygame.image.load("galaxy 4.png").convert()
    x_coord = 50
    y_coord = 600

    #list of enemy sprites
    enemy_list = pygame.sprite.Group()
    
    #list of all sprites
    all_sprites_list = pygame.sprite.Group()
    

    #list of shots
    projectile_list = pygame.sprite.Group()

    # create player
    player = Player()
    all_sprites_list.add(player)
    
    # boolean that ends game loop
    done = False
    go = True
    reset= False
    #manage screen update
    clock = pygame.time.Clock()

    

    #how fast the player moves
    player_speed = 10
    xspeed=0
    yspeed=0
 
    # Enemy spawn position
    e_x_start = 20
    e_y_start = 20



    


    #score
    score = 0
    

    count = 0

    #should we shoot a projectile?
    shoot=False


    #number of enemies

    # -----Main Loop -----
    while not done:
        
        # --- Main event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True #this ends the loop
            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xspeed = -player_speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xspeed = player_speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    yspeed = -player_speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    yspeed = player_speed

				#create projectile if spacebar is held down and there are no other projectiles
                elif event.key == pygame.K_SPACE:
       				shoot = projectile_list.__len__() == 0
                elif event.key == pygame.K_r:
                	reset = player.health<=0


            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    xspeed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    yspeed = 0

        


        
        
        #player movement
        
        # --Game logic goes here

        #if the player is alive
        if player.health>0:

        	#movement
        	if x_coord + xspeed > 0 and x_coord + xspeed < 1175:
        		x_coord+=xspeed
			if y_coord + yspeed > 0 and y_coord + yspeed < 625: 
				y_coord+=yspeed
			player.rect.x=x_coord
			player.rect.y=y_coord

			#create a new player projectile if we need to
	        if shoot:
	        	projectile = Projectile()
	     		projectile.rect.x = x_coord +player.rect.width/2
	       		projectile.rect.y = y_coord
	        	projectile_list.add(projectile)
	        	all_sprites_list.add(projectile)
	        	shoot = False


	       #update projectile
	        for p in projectile_list:
	            if Projectile.update(p):
	                projectile_list.remove(p)
	                all_sprites_list.remove(p) 


	        #update enemy
	        for e in enemy_list:
	        	#if it's offscreen, delete it
	            if Enemy.update(e):
	                enemy_list.remove(e)
	                all_sprites_list.remove(e)
	                player.health -=1


	            
	            #check if it's been hit by projectile
	            else:
	                projectiles_hit_list = pygame.sprite.spritecollide(e, projectile_list, True)
	                for p in projectiles_hit_list:
	                    if Enemy.collide(e):
	                        score += 100
	                        enemy_list.remove(e)
	                        all_sprites_list.remove(e)

	        #check if player hit by enemy (only relevant for the other type of motion or if things change)
	        enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
	        for e in enemy_hit_list:
	        	player.health-=1


    	    #make new enemy       

	        count += 1
	        if(len(enemy_list)<50 and count%50==0):

	            enemy = Enemy(x_coord,y_coord)
	            enemy.rect.x = e_x_start
	            enemy.rect.y = e_y_start
	            enemy_list.add(enemy)
	            all_sprites_list.add(enemy)


	        #update score (and count for test purposes)
	        text = font.render("Current score: " + str(score) +" Count: " + str(count) + " Health: " +str(player.health),True, WHITE)
        
        else:
	        text = font.render("Game over! You scored " + str(score) +" points. Press R to play again!",True, WHITE)
	        if reset:
	        	enemy_list.empty()
	        	projectile_list.empty()
	        	all_sprites_list.empty()
	        	player = Player()
    			all_sprites_list.add(player)
    			reset = False
    			score = 0
    			count = 0




	            
	        # --Drawing goes here        
    	screen.blit(background_image, [0, 0])
    	all_sprites_list.draw(screen)

    	screen.blit(text, (600, 600))

    	pygame.display.flip()

    	clock.tick(40)


    pygame.quit()

if __name__ == "__main__":
    main()
