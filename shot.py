import pygame
from circleshape import CircleShape
from constants import *

# Base class for shot objects
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius= SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)