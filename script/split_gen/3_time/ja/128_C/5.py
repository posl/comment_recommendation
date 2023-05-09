def solve():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i & (1<<(S[j][k]-1)):
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
