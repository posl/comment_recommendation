def main():
    n, p, q, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    d = [0] * n
    b[0] = a[0]
    c[0] = a[0] + a[1]
    d[0] = a[0] + a[1] + a[2]
    for i in range(1, n):
        b[i] = max(a[i], b[i - 1])
        c[i] = max(b[i - 1] + a[i], c[i - 1])
        d[i] = max(c[i - 1] + a[i], d[i - 1])
    ans = 0
    for i in range(n):
        ans = max(ans, p * b[i] + q * c[i] + r * d[i])
    print(ans)
