import pyglet
import random
from physicalobject import PhysicalObject
window_x = 800
window_y = 600
game_window = pyglet.window.Window(window_x, window_y)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def points(num_points):
    points = []
    for i in range(num_points):
        point_x = random.randint(10, window_x-10)
        point_y = random.randint(10, window_y-10)
        new_point = PhysicalObject(mass=0.0, forces=[], radius=2, x=point_x, y=point_y, batch=main_batch)
        new_point.velocity_x = random.randint(-400, 400)
        new_point.velocity_y = random.randint(-400, 400)
        points.append(new_point)
    return points


def update(dt, objects):
    for obj in objects:
        obj.update(dt)


if __name__ == '__main__':
    main_batch = pyglet.graphics.Batch()
    overlay = pyglet.text.Label(text="Matt's Amazing Text", x=10, y=10, batch=main_batch)
    points = points(100)
    pyglet.clock.schedule_interval(update, objects=points, interval=1/90.0)
    pyglet.app.run()
