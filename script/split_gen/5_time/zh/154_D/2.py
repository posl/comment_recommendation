def main():
    n, k = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + p[i + 1]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (s[i + k] - s[i]) / 2 + s[i])
    print(ans)
