def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (i + 1)) >= 5 * (10 ** i):
            x += 10 ** (i + 1) - x % (10 ** (i + 1))
        else:
            x -= x % (10 ** (i + 1))
    print(x)
