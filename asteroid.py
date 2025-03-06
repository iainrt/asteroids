import pygame
import circleshape as cs
from constants import *

# Base class for asteroid objects
class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",center=self.position, radius=2)

    def update(self, dt):
        self.position += (self.velocity * dt)