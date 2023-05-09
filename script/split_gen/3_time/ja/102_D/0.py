def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 9
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                p = s[i]
                q = s[j] - s[i]
                r = s[k] - s[j]
                s_ = s[n] - s[k]
                ans = min(ans, max(p, q, r, s_) - min(p, q, r, s_))
    print(ans)
