def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                continue
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])
            tmp.sort()
            for i in range(min(K - l - r, l + r)):
                if tmp[i] > 0:
                    break
                tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)
solve()
