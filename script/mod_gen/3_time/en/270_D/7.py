def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    #compute
    #dp[i] = the number of stones that Takahashi removes when the number of stones in the pile is i
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(K):
            if i - A[j] >= 0:
                if dp[i-A[j]] == 0:
                    dp[i] = 1
                    break
    #output
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")
    
main()

if __name__ == '__main__':
    main()