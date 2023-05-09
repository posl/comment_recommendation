def distance(a, b):
    result = 0
    for i in range(len(a)):
        result += (a[i] - b[i]) ** 2
    return result ** 0.5

if __name__ == '__main__':
    distance()