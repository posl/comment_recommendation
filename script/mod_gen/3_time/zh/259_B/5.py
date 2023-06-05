def rotatePoint(x, y, d):
    import math
    #math.pi为圆周率
    d = math.radians(d)
    x1 = x * math.cos(d) - y * math.sin(d)
    y1 = x * math.sin(d) + y * math.cos(d)
    return x1, y1
a, b, d = map(int, input().split())
x, y = rotatePoint(a, b, d)
print(x, y)

if __name__ == '__main__':
    rotatePoint()