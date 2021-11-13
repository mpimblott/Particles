import pyglet.gl
from arrow import Arrow


class ForcePointer(Arrow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
