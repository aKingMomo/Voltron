import pygame


#color definitions
BLACK = (0,0,0)
WHITE = (255,255,255)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("sprite.png").convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
    
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

    background_image = pygame.image.load("space_bg.jpg").convert()

    #list of enemy sprites
    enemy_list = pygame.sprite.Group()
    
    #list of all sprites
    all_sprites_list = pygame.sprite.Group()
    
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
    e_x_coord = 1130
    e_y_coord = -100
    x_coord = 10
    y_coord = 10
    
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
                    x_speed = -3
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 3
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_speed = -3
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_speed = 3
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_speed = 0
        
        # --Game logic goes here
        if x_coord + x_speed > 0 and x_coord + x_speed < 200:
            x_coord += x_speed
            player.rect.x = x_coord
        if y_coord + y_speed > 0 and y_coord + y_speed < 1180:
            y_coord += y_speed
            player.rect.y = y_coord
        for e in enemy_list:
            if e.rect.y >= 720:
                e.kill
                go = True
            else:
                e.rect.y += 5
                if e.rect.y%100 == 0:
                    go = True
                else:
                    go = False
        if(len(enemy_list)<50 and go):
            enemy = Enemy()
            enemy.rect.x = e_x_coord
            enemy.rect.y = e_y_coord
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
        # --Drawing goes here        
        screen.blit(background_image, [0, 0])
        all_sprites_list.draw(screen)
    
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
