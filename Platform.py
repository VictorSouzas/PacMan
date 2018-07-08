# -*- coding: utf-8 -*-

from pygame import Rect
from Entity import Entity


class Platform(Entity):
    def __init__(self, x, y, image):
        super(Entity, self).__init__()
        self.image = image
        # self.image.convert()
        # self.image.fill(Color(color))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass
