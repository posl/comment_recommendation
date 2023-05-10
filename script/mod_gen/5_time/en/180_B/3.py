def manhattan_distance(x, y):
    return sum(abs(x[i] - y[i]) for i in range(len(x)))

if __name__ == '__main__':
    manhattan_distance()