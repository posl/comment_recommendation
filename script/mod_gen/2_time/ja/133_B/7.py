def get_distance(a, b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i] - b[i]) ** 2
    return int(distance ** 0.5)

if __name__ == '__main__':
    get_distance()