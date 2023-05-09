def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        l = list(map(int, input().split()))
        C.append(l[0])
        A.append(l[1:])
    ans = 10**9 + 1
    for i in range(2**N):
        S = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    S[k] += A[j][k]
        if min(S) >= X:
            ans = min(ans, cost)
    if ans == 10**9 + 1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()