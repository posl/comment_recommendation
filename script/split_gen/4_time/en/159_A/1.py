def main():
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
    elif n == 1 and m == 1:
        print(0)
    elif n == 1 or m == 1:
        print(max(n, m) - 2)
    else:
        print((n - 2) * (m - 2))
