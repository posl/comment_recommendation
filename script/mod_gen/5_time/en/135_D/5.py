def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    DP = [[0 for i in range(13)] for j in range(N+1)]
    DP[0][0] = 1
    for i in range(1,N+1):
        c = S[i-1]
        if c == '?':
            for j in range(10):
                for k in range(13):
                    DP[i][(k*10+j)%13] += DP[i-1][k]
        else:
            j = int(c)
            for k in range(13):
                DP[i][(k*10+j)%13] += DP[i-1][k]
        for k in range(13):
            DP[i][k] %= MOD
    print(DP[N][5])
main()
