import argparse

from game import ConsoleGame, FIGURES


def config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', '--width', type=int, default=40, help='Width of Field')
    parser.add_argument('-H', '--height', type=int, default=10, help='Height of Field')
    parser.add_argument('-r', '--randomize', action='store_true', default=False, help='Create a random Field')
    parser.add_argument('-f', '--set_figure', choices=FIGURES, nargs='+', help='Set the figure on the Field')
    return parser


if __name__ == '__main__':
    parser = config()
    args = parser.parse_args()
    game = ConsoleGame(width=args.width, height=args.height, randomize=args.randomize)
    if args.set_figure:
        game.set_figures([(figure,) for figure in args.set_figure])
    game.run()
