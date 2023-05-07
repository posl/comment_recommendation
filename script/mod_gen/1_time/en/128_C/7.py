def solve():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for k in range(S[j][0]):
                if (i >> (S[j][k+1]-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()