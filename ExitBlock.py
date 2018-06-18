# -*- coding: utf-8 -*-

from Platform import Platform
from pygame import Color


class ExitBlock(Platform):

    def __init__(self, x, y):
        super(Platform, self).__init__(x, y)
        self.image.fill(Color("#0033FF"))
