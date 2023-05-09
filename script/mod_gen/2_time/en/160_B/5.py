def happiness_points(x):
    return 1000 * (x // 500) + 5 * (x % 500 // 5)

if __name__ == '__main__':
    happiness_points()