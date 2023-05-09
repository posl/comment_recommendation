def solve():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        S.append(list(map(int, input().split())))
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        tmp = 0
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i >> (S[j][k]-1) & 1:
                    cnt += 1
            if cnt % 2 == P[j]:
                tmp += 1
        if tmp == M:
            ans += 1
    print(ans)
solve()
