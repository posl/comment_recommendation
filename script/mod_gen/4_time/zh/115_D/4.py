def get_burger_level(n):
    if n == 0:
        return 1
    else:
        return 2 * get_burger_level(n-1) + 3

if __name__ == '__main__':
    get_burger_level()