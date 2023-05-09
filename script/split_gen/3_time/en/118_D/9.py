def makeInt(N, M, A):
    # N: length of matchstick
    # M: number of digits
    # A: digits
    # digit: matchstick
    digit = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # dp[i]: maximum number of matchstick
    # dp[i]: maximum number of matchstick
    dp = [-1] * (N + 1)
    dp[0] = 0
    # dp[i]: maximum number of matchstick
    digitList = [-1] * (N + 1)
    digitList[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + digit[A[j]] <= N:
                if dp[i + digit[A[j]]] < dp[i] * 10 + A[j]:
                    dp[i + digit[A[j]]] = dp[i] * 10 + A[j]
                    digitList[i + digit[A[j]]] = A[j]
    return digitList[N]
