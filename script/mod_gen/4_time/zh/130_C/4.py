def get_area(w, h, x, y):
    area = w * h / 2
    if x == w / 2 and y == h / 2:
        return area, 1
    else:
        return area, 0

if __name__ == '__main__':
    get_area()