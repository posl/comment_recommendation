def rotate(x, y, d):
    import math
    rad = math.radians(d)
    x_1 = x * math.cos(rad) - y * math.sin(rad)
    y_1 = x * math.sin(rad) + y * math.cos(rad)
    return x_1, y_1

if __name__ == '__main__':
    rotate()