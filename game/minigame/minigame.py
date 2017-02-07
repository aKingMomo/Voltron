import pygame


#color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)
CYAN = (0,255,255)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("sprite.png").convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.xspeed = 5
            self.yspeed = 0
            self.health = 3

    #updates position of enemy, returns True if past edge of screen
    def update(self):
       #check if past boundary (will be destroyed if past)
        if self.rect.x >= 1300:
            return True
        
        #move
        else:
            self.rect.x += self.xspeed
            self.rect.y += self.yspeed
            if self.rect.x == 1150: 
                self.xspeed = 0
                self.yspeed = 5
            if self.rect.y == 120:
                self.xspeed = -5
                self.yspeed = 0
            if self.rect.x == 10:
                self.xspeed = 0
                self.yspeed = 5
            if self.rect.y == 230:
                self.xspeed = 5
                self.yspeed = 0
            return False

    #called when hit by projectile, returns true if destroyed
    def collide(self):
            self.health -= 1
            if self.health == 0:
                return True
            else:
                return False



class Projectile(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([20,30])
            self.image.fill(CYAN)
            self.rect = self.image.get_rect()
            self.yspeed = -5

    #update the projectile, returns true if it has passed the top of the screen
    def update(self):
            if self.rect.y <= -self.rect.y:
                return True
            else:
                self.rect.y += self.yspeed
                return False


    
class Player(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("voltron.png").convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()

    
        
def main():
    pygame.init()

    size = (1280,720)
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Calibri', 25, True, False)


    background_image = pygame.image.load("space_bg.jpg").convert()

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
    #manage screen update
    clock = pygame.time.Clock()

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
 
    # Current position
    e_x_coord = 10
    e_y_coord = 10
    x_coord = 50
    y_coord = 600

    #are we shooting a projectile
    shoot = False

    #count for enemies
    ecount = 0

    #count for player
    pcount = 0

    #score
    score = 0
    
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
                    x_speed = -3
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 3
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_speed = -3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_speed = 3

                #if spacebar is down, start making new projectiles
                elif event.key == pygame.K_SPACE:
                    shoot = True
                   

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_speed = 0

                    #when the spacebar is released, stop making new things
                elif event.key == pygame.K_SPACE:
                    shoot = False
        
        # --Game logic goes here


        
        
        #player movement
        if x_coord + x_speed > 0 and x_coord + x_speed < 1100:
            x_coord += x_speed
            player.rect.x = x_coord
        #if y_coord + y_speed >  and y_coord + y_speed < 650:
         #   y_coord += y_speed
        player.rect.y = y_coord
        
        #create projectile if spacebar is held down and enough time has passed
        pcount -= 1
        if(shoot and pcount<=0):
            projectile = Projectile()
            projectile.rect.x = x_coord
            projectile.rect.y = y_coord
            projectile_list.add(projectile)
            all_sprites_list.add(projectile)
            pcount = 20


       #update projectile
        for p in projectile_list:
            if Projectile.update(p):
                projectile_list.remove(p)
                all_sprites_list.remove(p) 


        #update enemy
        for e in enemy_list:

            if Enemy.update(e):
                enemy_list.remove(e)
                all_sprites_list.remove(e)
                score -=500
            
            #check if it's been hit
            else:
                projectiles_hit_list = pygame.sprite.spritecollide(e, projectile_list, True)
                for p in projectiles_hit_list:
                    if Enemy.collide(e):
                        score += 100
                        enemy_list.remove(e)
                        all_sprites_list.remove(e)

        #make new enemy       
        ecount += 1

        if(len(enemy_list)<50 and ecount%50==0):
            enemy = Enemy()
            enemy.rect.x = e_x_coord
            enemy.rect.y = e_y_coord
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)

        #update score (and count for test purposes)
        text = font.render("Current score: " + str(score) +" Count: " + str(ecount),True, WHITE)


            
        # --Drawing goes here        
        screen.blit(background_image, [0, 0])
        all_sprites_list.draw(screen)
        screen.blit(text, (600, 600))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
