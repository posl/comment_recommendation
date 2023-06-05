def get_distance(d, x1, x2):
    distance = 0
    for i in range(d):
        distance += (x1[i] - x2[i]) ** 2
    return int(distance ** 0.5)

if __name__ == '__main__':
    get_distance()