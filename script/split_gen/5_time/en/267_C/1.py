def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * (n + 1)
    for i in range(n):
        t[i + 1] = min(t[i], s[i + 1])
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, s[i] - t[i])
    print(ans)
