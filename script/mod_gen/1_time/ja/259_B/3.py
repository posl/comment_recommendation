def rotate(x, y, r):
    import math
    x1 = x * math.cos(math.radians(r)) - y * math.sin(math.radians(r))
    y1 = x * math.sin(math.radians(r)) + y * math.cos(math.radians(r))
    return x1, y1
a, b, d = map(int, input().split())
x1, y1 = rotate(a, b, d)
print(x1, y1)

if __name__ == '__main__':
    rotate()