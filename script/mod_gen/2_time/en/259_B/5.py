def rotate(a, b, d):
    from math import sin, cos, radians
    d = radians(d)
    a, b = a * cos(d) - b * sin(d), a * sin(d) + b * cos(d)
    return a, b
a, b, d = map(int, input().split())
a, b = rotate(a, b, d)
print(a, b)

if __name__ == '__main__':
    rotate()