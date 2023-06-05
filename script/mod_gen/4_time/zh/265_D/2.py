def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [0]*n
    dp[0] = a[0]
    for i in range(1,n):
        dp[i] = dp[i-1] + a[i]
    #print(dp)
    ans = 0
    for i in range(n-1,2,-1):
        if dp[i] >= r:
            for j in range(i-1,1,-1):
                if dp[j] >= q+dp[i]:
                    for k in range(j-1,0,-1):
                        if dp[k] >= p+dp[j]:
                            ans = 1
                            break
                    if ans == 1:
                        break
                if ans == 1:
                    break
        if ans == 1:
            break
    if ans == 1:
        print("Yes")
    else:
        print("No")
main()
