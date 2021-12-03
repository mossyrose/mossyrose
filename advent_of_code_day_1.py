""" Advent of Code 2021 Day 1

How many measurements are increasing?

"""
import sys


def get_data(filename):
    """Read in data from 'filename', split lines
    into list elements, and convert elements from
    strings to integers.

    """
    with open(filename) as fname:
        data = fname.read()
    data = data.split("\n")
    if data[-1] == '':
        del data[-1]
    data = [int(i) for i in data]
    return data


def calculate_single_increases(data):
    """Count the number of 'data' elements that are
    larger than the previous element.

    """
    increasing_count = 0
    for index in range(1, len(data)):
        if data[index] > data[index-1]:
            increasing_count += 1
    return increasing_count


def calculate_triple_increases(data):
    """Count the number of triplets that are larger
    than the previous triplet.

    A triplet is the sum of three consecutive list
    elements. Windows slide by one element each step.

    """
    tri_increasing_count = 0
    this_triplet = 0
    previous_triplet = data[0] + data[1] + data[2]
    for index in range(3, len(data)):
        this_triplet = data[index] + data[index-1] + data[index-2]
        if (this_triplet) > (previous_triplet):
            tri_increasing_count += 1
        previous_triplet = this_triplet
    return tri_increasing_count


def main(sonar_readings):
    """Get the number of increases within a data set
    provided in 'filename'.

    Gets both single data increases and triple data
    increases. Prints both to screen.
    'filename' needs one measurement per line.

    """
    depths = get_data(sonar_readings)
    single_increases = calculate_single_increases(depths)
    print(f'The number of measurements that increase from the previous: {single_increases}\n')

    triple_increases = calculate_triple_increases(depths)
    print('The number of triple-measurement-sums that increase ' +
          f'from the previous: {triple_increases}')


if __name__ == "__main__":
    sonar_data = sys.argv[1]
    main(sonar_data)
    