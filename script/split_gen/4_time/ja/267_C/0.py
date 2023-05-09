def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = -10 ** 18
    for i in range(1, n - m + 2):
        ans = max(ans, s[i + m - 1] - s[i - 1] + sum(range(m)))
    print(ans)
