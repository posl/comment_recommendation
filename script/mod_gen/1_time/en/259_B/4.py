def rotate(x, y, angle):
    import math
    angle = math.radians(angle)
    x1 = x * math.cos(angle) - y * math.sin(angle)
    y1 = x * math.sin(angle) + y * math.cos(angle)
    return x1, y1
a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

if __name__ == '__main__':
    rotate()