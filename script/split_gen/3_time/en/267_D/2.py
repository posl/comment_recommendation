def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + (i + 1)
    c = [0] * (n - m + 1)
    for i in range(n - m + 1):
        c[i] = b[i] + b[i + m - 1]
    print(max(c))
