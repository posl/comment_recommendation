def manhattan_distance(x, y):
    return sum(abs(x[i] - y[i]) for i in range(len(x)))
