def get_max_num(N, M, A):
    Max = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    A.sort(reverse=True)
    #print(A)
    dp = [-1 for i in range(N+1)]
    dp[0] = 0
    for i in range(N+1):
        for j in range(M):
            if i-Max[A[j]-1] >= 0 and dp[i-Max[A[j]-1]] != -1:
                dp[i] = max(dp[i], dp[i-Max[A[j]-1]]+1)
    #print(dp)
    num = []
    if dp[N] == -1:
        return -1
    while N > 0:
        for i in range(M):
            if N >= Max[A[i]-1] and dp[N-Max[A[i]-1]] == dp[N]-1:
                num.append(A[i])
                N -= Max[A[i]-1]
                break
    num.sort(reverse=True)
    return num

if __name__ == '__main__':
    get_max_num()