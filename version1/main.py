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
        point_x = random.randint(0, window_x)
        point_y = random.randint(0, window_y)
        new_point = PhysicalObject(radius=1, x=point_x, y=point_y, batch=main_batch)
        new_point.velocity_x = random.random()*120
        new_point.velocity_y = random.random()*120
        points.append(new_point)
    return points


def update(dt, objects):
    for obj in objects:
        obj.update(dt)


if __name__ == '__main__':
    main_batch = pyglet.graphics.Batch()
    overlay = pyglet.text.Label(text="Render Demo", x=10, y=10, batch=main_batch)
    points = points(200)
    pyglet.clock.schedule_interval(update, objects=points, interval=1/60.0)
    pyglet.app.run()
