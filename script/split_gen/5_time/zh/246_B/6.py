def main():
    A, B = map(int, input().split())
    x = A / (A ** 2 + B ** 2) ** 0.5
    y = B / (A ** 2 + B ** 2) ** 0.5
    print("{0:.12f} {1:.12f}".format(x, y))
