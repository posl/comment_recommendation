def ManhattanDistance(n, x):
    d = 0
    for i in range(n):
        d += abs(x[i])
    return d

if __name__ == '__main__':
    ManhattanDistance()