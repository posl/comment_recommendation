def main():
    a, b, h, m = map(int, input().split())
    from math import cos, pi
    x = (h + m / 60) * pi / 6
    y = m * pi / 30
    from math import sqrt
    print(sqrt(a**2 + b**2 - 2 * a * b * cos(x - y)))
