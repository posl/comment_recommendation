def rotate(x, y, p):
    import math
    p = p * math.pi / 180
    return (x * math.cos(p) - y * math.sin(p), x * math.sin(p) + y * math.cos(p))

if __name__ == '__main__':
    rotate()