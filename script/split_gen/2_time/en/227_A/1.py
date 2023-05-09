def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        if (k - n) % (n - 1) == 0:
            print(n)
        else:
            print((k - n) % (n - 1) + 1)
