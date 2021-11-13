import math


class Force:
    def __init__(self, magnitude, direction, falloff=0.0):
        self.magnitude = magnitude
        self.direction = direction
        self.falloff = falloff

    def apply(self, particle):
        acceleration = (0, 0)
        angle = math.atan(self.direction[1]/self.direction[0])