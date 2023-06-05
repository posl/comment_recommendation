def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K)+1):
        for r in range(min(N, K)-l+1):
            now = 0
            Vl = V[:l]
            Vr = V[N-r:]
            Vl.sort()
            Vr.sort()
            for i in range(K-l-r):
                if i < len(Vl) and Vl[i] < 0:
                    Vl[i] = 0
                if i < len(Vr) and Vr[i] < 0:
                    Vr[i] = 0
            now += sum(Vl) + sum(Vr)
            Vl.sort(reverse=True)
            Vr.sort(reverse=True)
            for i in range(min(K-l-r, len(Vl))):
                now -= Vl[i]
            for i in range(min(K-l-r, len(Vr))):
                now -= Vr[i]
            ans = max(ans, now)
    print(ans)
solve()
