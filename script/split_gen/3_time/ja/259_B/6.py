def main():
    a,b,d = map(int, input().split())
    from math import sin, cos, pi
    rad = d * pi / 180
    x = a * cos(rad) - b * sin(rad)
    y = a * sin(rad) + b * cos(rad)
    print(x,y)
main()
