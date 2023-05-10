def rotate(x, y, d):
    import math
    r = math.radians(d)
    x1 = x*math.cos(r) - y*math.sin(r)
    y1 = x*math.sin(r) + y*math.cos(r)
    return x1, y1
a, b, d = map(int, input().split())
x, y = rotate(a, b, d)
print(x, y)

if __name__ == '__main__':
    rotate()