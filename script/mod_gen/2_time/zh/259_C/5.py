def rotate(x, y, d):
    import math
    d = math.radians(d)
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1
x, y, d = map(int, input().split())
x1, y1 = rotate(x, y, d)
print(x1, y1)

if __name__ == '__main__':
    rotate()