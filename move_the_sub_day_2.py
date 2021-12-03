"""Where is this submarine heading?!

Follow the coordinates and find the final horizontal
position and depth.

"""
import sys


def parse_moves(moves_file):
    """From 'moves_file', get a list of move instructions.

    Each line in the file should be "word n", where n is
    a number. Return the instructions as a list formatted as
    ["word", n], where n is an integer type.

    """
    with open(moves_file) as mvs:
        moves = mvs.read()
    moves = moves.split("\n")
    moves = [i.split() for i in moves]
    for values in moves:
        values[1] = int(values[1])
    return moves


def move_submarine(moves):
    """Move the submarine according to the instructions in 'moves'.

    Each move will be a word and an integer. Words must be one of
    "forward, up, down."
    Forward moves the submarine horizontally, and increases the
    depth by the product of the aim and the value given.
    Up decreases the aim by the given value.
    Down increases the aim by the given value.
    Return the final depth, horizonal positions, and aim.

    """
    depth = 0
    horiz = 0
    aim = 0

    for move in moves:
        if move[0] == "forward":
            horiz = horiz + move[1]
            depth = depth + (aim * move[1])
        elif move[0] == "up":
            aim = aim - move[1]
        elif move[0] == "down":
            aim = aim + move[1]
        else:
            # skip the step, I guess!
            pass
    return depth, horiz, aim


def main(moves_file):
    """Find the final position of the submarine based on 'moves_file',
    a file of directions. Also provide the product of the depth
    and horizontal position.

    """
    sub_moves = parse_moves(moves_file)
    depth, horiz, aim = move_submarine(sub_moves)
    print("Final position (depth, horizontal, aim): " +
          f"({depth}, {horiz}, {aim})")
    print(f"The product of those: {depth * horiz}")


if __name__ == "__main__":
    submarine_moves = sys.argv[1]
    main(submarine_moves)
