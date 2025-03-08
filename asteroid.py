import pygame
import circleshape as cs
from constants import *
import random

# Base class for asteroid objects
class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        old_velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: # spawn new smaller asteroids
            angle = random.uniform(20, 50)
            new_velocity_1 = old_velocity.rotate(angle) * 1.2
            new_velocity_2 = old_velocity.rotate(-angle) * 1.2
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_velocity_1
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2.velocity = new_velocity_2

