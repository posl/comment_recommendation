def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K)+1):
        for r in range(min(N, K)-l+1):
            a = V[:l]
            b = V[N-r:]
            c = V[l:N-r]
            for i in range(min(K-l-r, min(l, r))):
                if a[i] < b[i]:
                    a[i], b[i] = b[i], a[i]
            a.sort()
            b.sort(reverse=True)
            for i in range(min(K-l-r, len(c))):
                if c[i] < b[i]:
                    c[i], b[i] = b[i], c[i]
            ans = max(ans, sum(a)+sum(b))
    print(ans)
solve()
