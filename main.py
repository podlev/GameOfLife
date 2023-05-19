import os
import time

DELAY = 0.02
WIDTH = 20
HEIGHT = 10


class Cell:
    def __init__(self, is_alive=False):
        self.is_alive = is_alive

    def __repr__(self):
        if self.is_alive:
            return '*'
        else:
            return ' '


class Field:
    def __init__(self, width, height, set_random):
        self.width = width
        self.height = height
        if set_random:
            self.field = [[Cell(is_alive=False)] * self.width for _ in range(self.height)]
        else:
            self.field = [[Cell(is_alive=False)] * self.width for _ in range(self.height)]

    def set_planer(self):
        x = self.width // 2
        y = self.height // 2
        coordinates = [(y - 1, x + 1), (y, x - 1), (y, x + 1), (y + 1, x), (y + 1, x + 1)]
        for x, y in coordinates:
            self.field[x][y] = Cell(is_alive=True)

    def set_rpentamino(self):
        x = self.width // 2
        y = self.height // 2
        coordinates = [(y - 1, x), (y, x), (y, x + 1), (y + 1, x - 1), (y + 1, x)]
        for x, y in coordinates:
            self.field[x][y] = Cell(is_alive=True)

    def get_neighbours_count(self, row, col):
        neighbours = []
        for _row in range(-1, 2):
            for _col in range(-1, 2):
                if _row == 0 and _col == 0:
                    continue
                cell = self.field[(row + _row) % self.height][(col + _col) % self.width]
                if cell.is_alive:
                    neighbours.append(cell)
        return len(neighbours)

    def get_next_generation(self):
        new_field = [[Cell(is_alive=False)] * self.width for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                neighbours_count = self.get_neighbours_count(row, col)
                if self.field[row][col].is_alive and neighbours_count == 2 or neighbours_count == 3:
                    new_field[row][col] = Cell(is_alive=True)
                else:
                    new_field[row][col] = Cell(is_alive=False)
        return new_field


class Game:
    def __init__(self, set_figure, set_random=False):
        self.game_field = Field(WIDTH, HEIGHT, set_random)
        if set_figure in ['planner']:
            self.game_field.set_planer()

    def next_frame(self):
        self.game_field.field = self.game_field.get_next_generation()

    def draw(self):
        for row in range(-1, self.game_field.height + 1):
            for col in range(-1, self.game_field.width + 1):
                if row in [-1, self.game_field.height] or col in [-1, self.game_field.width]:
                    cell = '#'
                else:
                    cell = self.game_field.field[row][col]
                print(cell, end='')
            print()

    @staticmethod
    def clear():
        os.system('cls||clear')

    def run(self, step_by_step=False):
        while True:
            self.draw()
            self.next_frame()
            input() if step_by_step else time.sleep(DELAY)
            Game.clear()


if __name__ == '__main__':
    game = Game(set_figure='planner')
    game.run(step_by_step=False)
