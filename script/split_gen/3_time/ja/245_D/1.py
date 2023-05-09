def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    b[0] = c[0] // a[n]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i - j] -= a[n - j] * b[i - 1]
        b[i] = c[i] // a[n]
    print(*b)
