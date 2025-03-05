# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_instance = player.Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = "black")
        player_instance.draw(screen)
        pygame.display.flip()
        
        # limit framerate to 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()