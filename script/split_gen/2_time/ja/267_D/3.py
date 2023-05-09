def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
        for j in range(i):
            b[i] += a[j]
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[i]
    for i in range(m, n):
        ans = max(ans, ans + b[i] - b[i - m])
    print(ans)
