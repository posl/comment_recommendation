def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    d = {}
    for i in range(n + 1):
        r = s[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for r in d:
        ans += d[r] * (d[r] - 1) // 2
    print(ans)
