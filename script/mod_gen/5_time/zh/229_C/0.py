def main():
    import sys
    N, W = map(int, sys.stdin.readline().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    #print(N, W)
    #dp = [[0 for i in range(W+1)] for j in range(N)]
    dp = [0 for i in range(W+1)]
    for i in range(N):
        for j in range(W, -1, -1):
            if j >= B[i]:
                dp[j] = max(dp[j], dp[j-B[i]] + A[i])
    print(dp[-1])
    #print(dp)

if __name__ == '__main__':
    main()