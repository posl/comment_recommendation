def main():
    import sys
    import numpy as np
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    T = np.zeros(N, dtype=np.int64)
    K = np.zeros(N, dtype=np.int64)
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        T[i], K[i], *A[i, :K[i]] = map(int, input().split())
    #print(N)
    #print(T)
    #print(K)
    #print(A)
    #dp[i]: ムーブiを習得するのに必要な最小時間
    dp = np.zeros(N, dtype=np.int64)
    dp[0] = T[0]
    #print(dp)
    #dp[i] = min(dp[j] + T[i]) for j in A[i]
    for i in range(1, N):
        dp[i] = dp[A[i, 0]] + T[i]
        for j in range(1, K[i]):
            dp[i] = min(dp[i], dp[A[i, j]] + T[i])
    #print(dp)
    print(dp[-1])

if __name__ == '__main__':
    main()