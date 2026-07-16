from typing import List


class Dungeon:
    def __init__(self, matrix, rooms=None):
        self.matrix = matrix  # 0 - стена, 1 - пол
        if rooms is not None:
            self.rooms = rooms
        else:
            self.rooms = []
        self.explored = set()

    def is_wall(self, x, y):
        if 0 <= y < len(self.matrix) and 0 <= x < len(self.matrix[0]):
            return self.matrix[y][x] == 0
        return True  # За границами считаем стеной