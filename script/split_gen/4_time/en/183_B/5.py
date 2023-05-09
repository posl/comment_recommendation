def main():
    from sys import stdin
    from math import atan2, degrees, pi
    from decimal import Decimal, getcontext
    getcontext().prec = 15
    S_x, S_y, G_x, G_y = map(int, stdin.readline().split())
    print(Decimal(S_x + G_x) / 2)
