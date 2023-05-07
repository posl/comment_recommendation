def can_reach(N, M, T, A, X, Y):
    #Takahashi can reach Room N if he can reach Room N-1.  
    #If he can reach Room N-1, he can reach Room N-2, and so on.
    #If he can reach Room 1, he can reach Room 2, and so on.
    #So, we can solve this problem by dynamic programming.
    #Let dp[i] be True if he can reach Room i, and False otherwise.
    #dp[i] = True if dp[i-1] is True and T-A[i-1] >= 0, or dp[X[j]] is True and T-Y[j] >= 0 for some j.
    #If dp[N] is True, he can reach Room N.
    #If dp[N] is False, he cannot reach Room N.
    dp = [False] * (N+1)
    dp[1] = True
    for i in range(2, N+1):
        if dp[i-1] and T-A[i-2] >= 0:
            dp[i] = True
        for j in range(M):
            if dp[X[j]] and T-Y[j] >= 0:
                dp[i] = True
    return dp[N]

if __name__ == '__main__':
    can_reach()