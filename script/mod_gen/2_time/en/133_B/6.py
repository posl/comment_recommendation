def distance(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5

if __name__ == '__main__':
    distance()