# -*- coding: utf-8 -*-

import Platform
from pygame import Color


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))
