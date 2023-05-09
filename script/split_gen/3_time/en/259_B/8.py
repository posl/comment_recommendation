def main():
    from math import cos, sin, pi
    a, b, d = [int(i) for i in input().split()]
    d = d * pi / 180
    print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
