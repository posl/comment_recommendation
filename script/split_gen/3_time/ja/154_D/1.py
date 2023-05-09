def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = [0] * n
    s[0] = (p[0] + 1) / 2
    for i in range(1, n):
        s[i] = s[i - 1] + (p[i] + 1) / 2
    ans = 0
    for i in range(n - k + 1):
        if i == 0:
            ans = max(ans, s[k - 1])
        else:
            ans = max(ans, s[i + k - 1] - s[i - 1])
    print(ans)
