def main():
    N,W = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    dp = [0] * (W+1)
    dp[0] = 1
    for i in A:
        for j in range(W,-1,-1):
            if dp[j] == 1 and j+i <= W:
                dp[j+i] = 1
    print(sum(dp))

if __name__ == '__main__':
    main()