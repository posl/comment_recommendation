def solve():
    S = input()
    MOD = 10**9+7
    Q = S.count('?')
    N = len(S)
    # DP[i][j] = (S[i:]について, '?'をj個Aに置き換えたときのABC数)
    DP = [[0] * (Q+1) for _ in range(N+1)]
    DP[N][Q] = 1
    for i in range(N-1, -1, -1):
        for j in range(Q+1):
            if S[i] == 'C':
                DP[i][j] = DP[i+1][j]
            elif S[i] == 'B':
                DP[i][j] = DP[i+1][j+1]
            elif S[i] == 'A':
                DP[i][j] = DP[i+1][j+2]
            else:
                DP[i][j] = (3 * DP[i+1][j] + DP[i+1][j+1] + DP[i+1][j+2]) % MOD
    print(DP[0][0])
solve()
