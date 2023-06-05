def minkowski(x, y, p):
    return sum([abs(xi - yi) ** p for xi, yi in zip(x, y)]) ** (1 / p)

if __name__ == '__main__':
    minkowski()