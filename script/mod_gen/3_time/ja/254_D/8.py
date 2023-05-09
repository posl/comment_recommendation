def find_squares(n):
    return [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

if __name__ == '__main__':
    find_squares()