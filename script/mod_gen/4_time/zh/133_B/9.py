def get_distance(x, y):
    distance = 0
    for i in range(len(x)):
        distance += (x[i] - y[i]) ** 2
    return distance ** 0.5

if __name__ == '__main__':
    get_distance()