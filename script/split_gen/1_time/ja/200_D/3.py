def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    dp = [[-1] * mod for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(mod):
            if dp[i][j] != -1:
                dp[i + 1][j] = dp[i][j]
            elif dp[i + 1][(j + A[i]) % mod] != -1:
                dp[i + 1][j] = i + 1
            else:
                dp[i + 1][j] = -1
    if dp[N][0] == -1:
        print('No')
        return
    print('Yes')
    B = []
    C = []
    i = N
    j = 0
    while i != 0:
        if dp[i][j] == i:
            B.append(i)
            j = (j - A[i - 1]) % mod
        else:
            C.append(i)
        i -= 1
    B.reverse()
    C.reverse()
    print(len(B), *B)
    print(len(C), *C)
