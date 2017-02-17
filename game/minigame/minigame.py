import pygame
import math
import random


# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

global enemy_speed
enemy_speed = 3.0
# character is name of player sprite file
# options:Castle, Red, Green, Blue, Yellow or Black
# TODO when adding to renpy: Select character based on points
character = "Black"


class Enemy(pygame.sprite.Sprite):
    def __init__(self, xtarget, ytarget):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Galra.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = float(random.randrange(0, 1280))
        self.rect.y = 0.0 - self.rect.height
        if xtarget - self.rect.x != 0:
            self.theta = math.atan(
                abs((ytarget - self.rect.y) / (xtarget - self.rect.x)))
            if xtarget - self.rect.x > 0:
                self.xspeed = math.cos(self.theta) * enemy_speed
            else:
                self.xspeed = - math.cos(self.theta) * enemy_speed

            self.yspeed = math.sin(self.theta) * enemy_speed
        else:
            self.yspeed = enemy_speed
            self.xspeed = 0

        self.health = 1

    # updates position of enemy, returns True if past edge of screen
    def update(self):
        # check if past boundary (will be destroyed)
        if self.rect.x >= 1300 or self.rect.x <= -100 or self.rect.y >= 800:
            return True
        else:
            self.rect.x += self.xspeed
            self.rect.y += self.yspeed
            return False

    # called when hit by projectile, returns true if to be destroyed
    def collide(self):
        self.health -= 1
        if self.health == 0:
            return True
        else:
            return False


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 30])
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.yspeed = -10

    # update the projectile position
    # returns true if it has passed the top of the screen
    def update(self):
        if self.rect.y <= -self.rect.y:
            return True
        else:
            self.rect.y += self.yspeed
            return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("%s.png" % (character)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.health = 5


def main():
    pygame.init()

    global enemy_speed
    size = (1280, 720)
    screen = pygame.display.set_mode(size)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    background_image = pygame.image.load("galaxy 4.png").convert()
    x_coord = 50
    y_coord = 600

    # list of enemy sprites
    enemy_list = pygame.sprite.Group()
    # list of all sprites
    all_sprites_list = pygame.sprite.Group()
    # list of shots
    projectile_list = pygame.sprite.Group()

    # create player
    player = Player()
    all_sprites_list.add(player)
    # booleans that alter game loop
    done = False
    pause = False
    reset = False
    # manage screen update
    clock = pygame.time.Clock()
    # how fast the player moves
    player_speed = 5
    xspeed = 0
    yspeed = 0
    # Enemy information - spawn timer and movespeed
    enemy_spawn = 50
    enemy_speed = 3.0
    # score
    score = 0
    # housekeeping variables (count is time, state is for game progression)
    count = 0
    state = 0
    # should we shoot a projectile?
    shoot = False

    # -----Main Loop -----
    while not done:
        # --- Main event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # this ends the loop
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

                # Create projectile if spacebar is held down
                # and you are allowed to have more by your score
                elif event.key == pygame.K_SPACE:
                    shoot = projectile_list.__len__() <= state / 2
                # Reset the game if the player is dead and presses R
                elif event.key == pygame.K_r:
                    reset = player.health <= 0
                # Pause/unpause the game if the player presses P
                elif event.key == pygame.K_p:
                    pause = not pause

            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    xspeed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    yspeed = 0

        # --Game logic goes here
        if pause:
            # TODO: Pause menu
            text = font.render(
                "The game is paused. Please press P to continue", True, WHITE)
        else:
            # If the player is dead, the gameover procedure
            if player.health < 0:
                text = font.render("Game over! You scored " + str(score) +
                                   " points. Press R to play again!", True, WHITE)
                # Return changed parameters to initial values to restart
                # TODO: countdown before restart?
                if reset:
                    enemy_list.empty()
                    projectile_list.empty()
                    all_sprites_list.empty()
                    player = Player()
                    all_sprites_list.add(player)
                    reset = False
                    score = 0
                    count = 0
                    xspeed = 0
                    yspeed = 0
                    x_coord = 50
                    y_coord = 600
                    state = 0

            # If the game is running and the player is alive
            else:
                # Player Movement
                if x_coord + xspeed > 0 and x_coord + xspeed < 1175:
                    x_coord += xspeed
                if y_coord + yspeed > 0 and y_coord + yspeed < 625:
                    y_coord += yspeed
                player.rect.x = x_coord
                player.rect.y = y_coord

                # Create a new player projectile if we need to
                if shoot:
                    projectile = Projectile()
                    projectile.rect.x = x_coord + player.rect.width / 2
                    projectile.rect.y = y_coord
                    projectile_list.add(projectile)
                    all_sprites_list.add(projectile)
                    shoot = False

                # Update projectile
                for p in projectile_list:
                    if Projectile.update(p):
                        projectile_list.remove(p)
                        all_sprites_list.remove(p)

                # Update enemy
                for e in enemy_list:
                    # If it's offscreen, delete it (maybe penalize player?)
                    if Enemy.update(e):
                        enemy_list.remove(e)
                        all_sprites_list.remove(e)

                    # Check if it's been hit by projectile
                    else:
                        projectiles_hit_list = pygame.sprite.spritecollide(
                            e, projectile_list, True)
                        for p in projectiles_hit_list:
                            if Enemy.collide(e):
                                score += 100
                                enemy_list.remove(e)
                                all_sprites_list.remove(e)

                # Check if player hit by enemy
                enemy_hit_list = pygame.sprite.spritecollide(
                    player, enemy_list, True)
                for e in enemy_hit_list:
                    player.health -= 1

                # Make new enemy, up to a max of ten
                # This spawns with a random X coordinate, above the screen
                # It moves towards the Player
                count += 1
                if(len(enemy_list) < 10 and count % enemy_spawn == 0):
                        # Calculate current speeds and state
                        # every 1K points, the enemies spawn sooner (max 6 per sec)
                        # every 2K, the enemies move faster
                        # every 2K you can shoot another projectile
                    state = score / 1000
                    enemy_spawn = 50 - 5 * state
                    if state >= 9:
                        enemy_spawn = 10
                    enemy_speed = 3.0 + 1.5 * (state / 2)

                    enemy = Enemy(x_coord, y_coord)
                    enemy_list.add(enemy)
                    all_sprites_list.add(enemy)

                # Update score (and test variables for test purposes)
                text = font.render("Current score: " + str(score) +
                                   " Count: " + str(count) +
                                   " Health: " + str(player.health) +
                                   " Enemy count: " + str(len(enemy_list)), True, WHITE)

        # --Drawing goes here
        screen.blit(background_image, [0, 0])
        all_sprites_list.draw(screen)

        screen.blit(text, (300, 600))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
