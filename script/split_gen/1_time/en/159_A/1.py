def main():
    n, m = map(int, input().split())
    if n == 0:
        print(m)
    elif m == 0:
        print(n)
    else:
        print((n * (n - 1) // 2) + (m * (m - 1) // 2))
