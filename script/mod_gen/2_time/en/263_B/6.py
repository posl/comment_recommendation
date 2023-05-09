def main():
    n = int(input())
    p = list(map(int,input().split()))
    if n==2:
        print(1)
        return
    p.insert(0,0)
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[p[i-1]]+1
    print(max(dp))
main()

if __name__ == '__main__':
    main()