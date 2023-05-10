def rotate(x, y, deg):
    rad = deg * math.pi / 180
    rx = x * math.cos(rad) - y * math.sin(rad)
    ry = x * math.sin(rad) + y * math.cos(rad)
    return rx, ry

if __name__ == '__main__':
    rotate()