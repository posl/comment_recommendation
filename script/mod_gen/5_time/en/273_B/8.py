def my_round(x, y):
    if x % y == 0:
        return x
    else:
        return int(x/y) * y + y

if __name__ == '__main__':
    my_round()