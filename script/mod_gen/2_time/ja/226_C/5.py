def main():
    N = int(input())
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K = map(int, input().split())
        A[i] = list(map(int, input().split()))
    #print(N)
    #print(T)
    #print(A)
    #print('-----')
    # dp[i] : i 番目の技を覚えるのに必要な最小時間
    dp = [0] * N
    for i in range(N):
        #print('i = ', i)
        if i == 0:
            dp[i] = T[i]
            #print('dp[i] = ', dp[i])
            continue
        # A[i] に含まれる技をすべて覚えてから i 番目の技を覚える
        dp[i] = min(dp[j - 1] for j in A[i]) + T[i]
        #print('dp[i] = ', dp[i])
    print(dp[-1])

if __name__ == '__main__':
    main()