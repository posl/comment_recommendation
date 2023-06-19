def get_new_coordinate(x, y, d):
    import math
    rad = d * math.pi / 180
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y

if __name__ == '__main__':
    get_new_coordinate()