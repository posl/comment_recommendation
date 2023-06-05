def distance(x, y):
    return sum((a-b)**2 for a, b in zip(x, y))**0.5

if __name__ == '__main__':
    distance()