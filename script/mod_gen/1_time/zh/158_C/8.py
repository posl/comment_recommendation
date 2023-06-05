def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
import math
import sys

if __name__ == '__main__':
    round_up()