from physicalobject import PhysicalObject


class Particle(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(1.0, [], *args, **kwargs)
