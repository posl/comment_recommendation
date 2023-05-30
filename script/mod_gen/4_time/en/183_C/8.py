def solve(N,K,T):
    import itertools
    ans = 0
    for p in itertools.permutations(range(1,N)):
        t = 0
        t += T[0][p[0]]
        for i in range(1,N-1):
            t += T[p[i-1]][p[i]]
        t += T[p[N-2]][0]
        if t == K:
            ans += 1
    return ans
N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]
print(solve(N,K,T))
