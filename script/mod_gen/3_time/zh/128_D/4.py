def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1 - l):
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(N - r, N):
                tmp.append(V[i])
            tmp.sort()
            for i in range(K - l - r):
                if i >= len(tmp):
                    break
                if tmp[i] < 0:
                    tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)
solve()
