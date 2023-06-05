def solve():
    N, M = map(int, input().split())
    K = []
    S = []
    P = list(map(int, input().split()))
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    ans = 0
    for i in range(2**N):
        on = [0]*M
        for j in range(N):
            if i>>j & 1:
                for k in range(M):
                    if j+1 in S[k]:
                        on[k] += 1
        if on == P:
            ans += 1
    print(ans)
solve()
