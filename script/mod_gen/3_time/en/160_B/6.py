def get_happiness_points(x):
    happiness_points = 0
    happiness_points += x // 500 * 1000
    happiness_points += x % 500 // 5 * 5
    return happiness_points

if __name__ == '__main__':
    get_happiness_points()