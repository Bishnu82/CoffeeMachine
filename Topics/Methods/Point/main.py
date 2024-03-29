import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point_2):
        return math.sqrt((self.x - point_2.x)**2 + (self.y - point_2.y)**2)
