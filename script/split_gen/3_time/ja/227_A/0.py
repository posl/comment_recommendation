def main():
    n, k, a = map(int, input().split())
    if (k % n + a - 1) % n == 0:
        print(n)
    else:
        print((k % n + a - 1) % n)
