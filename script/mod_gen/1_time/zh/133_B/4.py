def calcDist(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i])**2
    return dist**0.5

if __name__ == '__main__':
    calcDist()