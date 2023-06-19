def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    if n <= k:
        print(len(set(c)))
        return
    d = dict()
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    ans = len(d)
    for i in range(n - k):
        if c[i] in d:
            d[c[i]] -= 1
            if d[c[i]] == 0:
                del d[c[i]]
        if c[i + k] in d:
            d[c[i + k]] += 1
        else:
            d[c[i + k]] = 1
        ans = max(ans, len(d))
    print(ans)

if __name__ == '__main__':
    solve()