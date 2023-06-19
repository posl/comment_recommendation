def rotate(x, y, d):
    import math
    d = math.radians(d)
    x2 = x * math.cos(d) - y * math.sin(d)
    y2 = x * math.sin(d) + y * math.cos(d)
    return x2, y2
a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

if __name__ == '__main__':
    rotate()