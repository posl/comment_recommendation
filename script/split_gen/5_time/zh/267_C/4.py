def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    for i in range(1, m + 1):
        ans = max(ans, s[i] - min(s[:i]))
    for i in range(m + 1, n + 1):
        ans = max(ans, s[i] - min(s[i - m:i]))
    print(ans)
