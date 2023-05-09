def solve():
    N, M = map(int, input().split())
    K = []
    S = []
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        cnt = 0
        for j in range(M):
            on = 0
            for k in range(K[j]):
                if i & (1 << (S[j][k] - 1)):
                    on += 1
            if on % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)
