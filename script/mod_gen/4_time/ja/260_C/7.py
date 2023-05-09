def calc_blue_gem(level, red, blue, x, y):
    if level == 1:
        return blue
    elif level == 2:
        return blue + red * x
    else:
        return calc_blue_gem(level-1, red, blue, x, y) * y + calc_blue_gem(level-2, red, blue, x, y) * x

if __name__ == '__main__':
    calc_blue_gem()