def main():
    x, k = map(int, input().split())
    y = x
    for i in range(k):
        if y % (10 ** (i + 1)) >= 5 * (10 ** i):
            y = y // (10 ** (i + 1)) * (10 ** (i + 1)) + (10 ** (i + 1))
        else:
            y = y // (10 ** (i + 1)) * (10 ** (i + 1))
    print(y)
