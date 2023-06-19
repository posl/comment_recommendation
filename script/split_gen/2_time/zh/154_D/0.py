def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + p[i] / p[i - 1]
    ans = 0
    for i in range(k, n + 1):
        ans = max(ans, s[i] - s[i - k])
    print(ans)
