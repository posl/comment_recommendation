def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = 1
    ans = len(d)
    for i in range(k, n):
        d[c[i]] = 1
        if d[c[i-k]] == 1:
            del d[c[i-k]]
        ans = max(ans, len(d))
    return ans
print(solve())

if __name__ == '__main__':
    solve()