def rotate(x, y, d):
    import math
    pi = math.pi
    r = d * pi / 180
    x1 = x * math.cos(r) - y * math.sin(r)
    y1 = x * math.sin(r) + y * math.cos(r)
    return x1, y1

if __name__ == '__main__':
    rotate()