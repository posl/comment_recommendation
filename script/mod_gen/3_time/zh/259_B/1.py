def rotate(a, b, d):
    import math
    x = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
    y = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
    return x, y

if __name__ == '__main__':
    rotate()