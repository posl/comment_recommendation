def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(K+1):
        for b in range(K+1-a):
            c = K-a-b
            l = sorted([V[i] for i in range(a)])
            r = sorted([V[i] for i in range(N-b, N)], reverse=True)
            s = sum(l)+sum(r)
            for _ in range(min(c, len(l), len(r))):
                if l[_] < r[_]:
                    s += r[_]-l[_]
                else:
                    break
            ans = max(ans, s)
    print(ans)
solve()
