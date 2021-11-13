import pyglet.shapes


class PhysicalObject(pyglet.shapes.Circle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def check_bounds(self, window_x=800, window_y=600):
        min_x = -self.radius/2
        min_y = -self.radius/2
        max_x = window_x + self.radius/2
        max_y = window_y + self.radius/2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()
