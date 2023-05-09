def solve():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    S = [0]
    for i in range(N):
        S.append((S[-1]+A[i])%M)
    from collections import defaultdict
    D = defaultdict(int)
    for s in S:
        D[s] += 1
    ans = 0
    for k,v in D.items():
        ans += v*(v-1)//2
    print(ans)
