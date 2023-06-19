def get_point(a, b):
    x = 0
    y = 0
    if a == 0:
        x = 0
        y = b
    elif b == 0:
        x = a
        y = 0
    else:
        x = a * b / (a ** 2 + b ** 2) ** 0.5
        y = (a ** 2 - x ** 2) ** 0.5
    return x, y

if __name__ == '__main__':
    get_point()