import argparse

from game import Game, FIGURES

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--randomize', action='store_true', help='Create a random Field')
parser.add_argument('-r', '--randomize', action='store_true', help='Create a random Field')
parser.add_argument('-f', '--set_figure', choices=FIGURES, help='Set the figure on the Field')
args = parser.parse_args()
print(args.r)

