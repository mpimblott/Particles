import pyglet.shapes


class PhysicalObject(pyglet.shapes.Circle):
    def __init__(self, mass, forces, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.mass = mass
        self.forces = forces

    def check_bounds(self, window_x=800, window_y=600):
        min_x = 0
        min_y = 0
        max_x = window_x
        max_y = window_y
        if self.x < min_x:
            # hit left boundary
            self.velocity_x = -self.velocity_x
        elif self.x > max_x:
            # hit right boundary
            self.velocity_x = -self.velocity_x
        if self.y < min_y:
            # hit bottom boundary
            self.velocity_y = -self.velocity_y
        elif self.y > max_y:
            # hit top boundary
            self.velocity_y = -self.velocity_y

    def move(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def accelerate(self):
        acceleration = (0, 0)
        for force in self.forces:
            acceleration += force.accelerate()
        self.velocity_x += acceleration[0]
        self.velocity_y += acceleration[1]

    def update(self, dt):
        # update acceleration based on forces
        # move based on current velocity
        self.move(dt)
        # keep in the window
        self.check_bounds()
