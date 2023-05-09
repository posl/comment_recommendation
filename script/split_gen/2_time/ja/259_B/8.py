def rotate(x, y, d):
    from math import cos, sin, radians
    a = cos(radians(d))
    b = sin(radians(d))
    return a*x - b*y, b*x + a*y
a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)
