def solve():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s[1:])
        P.append(int(input()))
    S = list(zip(*S))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in S[j]:
                if (i >> (k - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
