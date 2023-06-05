def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [a[0]]
    for i in range(1, n):
        s.append(s[i-1] + a[i])
    r = [x % m for x in s]
    from collections import Counter
    c = Counter(r)
    ans = 0
    for x in c:
        if x == 0:
            ans += c[x]
        ans += c[x] * (c[x] - 1) // 2
    print(ans)
