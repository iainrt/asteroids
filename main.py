# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # link groups to Player and Asteroid classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create the objects
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, shots_group)
    asteroid_field = AsteroidField()
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for object in asteroids:
            if player.collision_check(object):
                print("Game over!")
                sys.exit()
            for bullet in shots_group:
                if bullet.collision_check(object):
                    object.split()
                    bullet.kill()

        # Update shots
        for shot in shots_group:
            shot.update(dt)

        screen.fill(color = "black")

        # Draw shots
        for shot in shots_group:
            shot.draw(screen)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        # limit framerate to 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()