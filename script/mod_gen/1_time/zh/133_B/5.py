def distance(x, y):
    d = 0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return d ** 0.5

if __name__ == '__main__':
    distance()