def rotate(x, y, p):
    import math
    rad = math.radians(p)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

if __name__ == '__main__':
    rotate()