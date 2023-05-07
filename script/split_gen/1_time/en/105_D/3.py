def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N+1):
        d[S[i]%M] += 1
    ans = 0
    for k,v in d.items():
        ans += v*(v-1)//2
    print(ans)
