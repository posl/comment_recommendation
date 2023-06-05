def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    dp = [0]*N
    dp[0] = T
    for i in range(N-1):
        dp[i+1] = min(dp[i]+A[i],T)
    for x,y in XY:
        if dp[x-1]+y>=T:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()