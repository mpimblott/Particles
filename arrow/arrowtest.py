import pyglet
import math
game_window = pyglet.window.Window(800, 600)
x1 = 300
y1 = 300


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


if __name__ == '__main__':
    main_batch = pyglet.graphics.Batch()
    arrow_points = (x1, y1, x1, y1 + 150, x1, y1 + 150, x1 + 40, y1 + 100, x1, y1 + 150, x1 - 40, y1 + 100)
    arrow1 = main_batch.add(6, pyglet.gl.GL_LINES, None,
                            ('v2f', arrow_points),
                            # ('c3B', (0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
                            )
    pyglet.app.run()
