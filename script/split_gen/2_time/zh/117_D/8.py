def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    if n == 1:
        print(min(abs(x[i] - x[i + n - 1]) for i in range(m - n + 1)))
        return
    if n == 2:
        print(min(abs(x[i] - x[i + n - 1]) + abs(x[i + n - 1] - x[i + n]) for i in range(m - n + 2)))
        return
    print(min(abs(x[i] - x[i + n - 1]) + abs(x[i + n - 1] - x[i + n]) + abs(x[i + n] - x[i + n + 1]) for i in range(m - n + 3)))
