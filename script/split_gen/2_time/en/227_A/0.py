def main():
    n, k, a = map(int, input().split())
    if (k - a) % (n - 1) == 0:
        print(n)
    else:
        print((k - a) % (n - 1) + a)
