def rotate(x, y, d):
    import math
    x1 = x * math.cos(math.radians(d)) - y * math.sin(math.radians(d))
    y1 = x * math.sin(math.radians(d)) + y * math.cos(math.radians(d))
    return (x1, y1)

if __name__ == '__main__':
    rotate()