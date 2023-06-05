def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    else:
        return (y2 - y1) / (x2 - x1)

if __name__ == '__main__':
    get_slope()