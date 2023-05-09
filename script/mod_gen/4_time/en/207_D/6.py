def rotate(a, b, p):
    import math
    return (a * math.cos(math.radians(p)) - b * math.sin(math.radians(p)), a * math.sin(math.radians(p)) + b * math.cos(math.radians(p)))

if __name__ == '__main__':
    rotate()