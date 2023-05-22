import os
import random
import time

DELAY = 0.1
WIDTH = 40
HEIGHT = 10

FIGURES = {'planner': lambda y, x: [(y - 1, x + 1), (y, x - 1), (y, x + 1), (y + 1, x), (y + 1, x + 1)],
           'r-pentamino': lambda y, x: [(y - 1, x), (y, x), (y, x + 1), (y + 1, x - 1), (y + 1, x)]}


class Cell:
    def __init__(self, is_alive=False):
        self.is_alive = is_alive

    def __repr__(self):
        return '*' if self.is_alive else ' '


class Field:
    def __init__(self, width, height, randomize=False):
        self.width, self.height = width, height
        self.field = [[Cell(is_alive=False)] * self.width for _ in range(self.height)]
        if randomize:
            for row in range(self.height):
                for col in range(self.width):
                    self.field[row][col] = Cell(is_alive=random.choice([True, False]))

    def set_figure(self, figure, row=None, col=None):
        if figure in FIGURES:
            if row is None and col is None:
                row, col = self.height // 2, self.width // 2
            for _row, _col in FIGURES[figure](row, col):
                if 0 <= _row < self.height and 0 <= _col < self.width:
                    self.field[_row][_col] = Cell(is_alive=True)

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

    def get_next_field(self):
        new_field = [[Cell(is_alive=False)] * self.width for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                neighbours_count = self.get_neighbours_count(row, col)
                if self.field[row][col].is_alive and neighbours_count == 2 or neighbours_count == 3:
                    new_field[row][col] = Cell(is_alive=True)
                else:
                    new_field[row][col] = Cell(is_alive=False)
        return new_field

    def step(self):
        self.field = self.get_next_field()


class ConsoleGame:
    def __init__(self, width, height, randomize=False):
        self.game_field = Field(width=width, height=height, randomize=randomize)

    def set_figures(self, figures):
        for figure in figures:
            self.game_field.set_figure(*figure)

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
            try:
                self.draw()
                self.game_field.step()
                input() if step_by_step else time.sleep(DELAY)
                self.clear()
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    game = ConsoleGame(width=WIDTH, height=HEIGHT, randomize=False)
    game.set_figures([('planner', 5, 1), ('r-pentamino',), ('planner', 100, 100)])
    game.run(step_by_step=False)
