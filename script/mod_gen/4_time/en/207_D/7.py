def rotate(point, angle):
    import math
    x, y = point
    rad = math.radians(angle)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

if __name__ == '__main__':
    rotate()