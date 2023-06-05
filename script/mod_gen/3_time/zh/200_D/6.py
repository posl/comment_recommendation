def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] % 200
    dp = [[0 for i in range(200)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(200):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
                dp[i][(j+a[i-1])%200] = 1
    #print(dp)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if dp[i][0] == 1 and dp[j][0] == 1:
                print("Yes")
                print(i, end=" ")
                for k in range(i):
                    if dp[k+1][0] == 1:
                        print(k+1, end=" ")
                print()
                print(j-i, end=" ")
                for k in range(i, j):
                    if dp[k+1][0] == 1:
                        print(k+1, end=" ")
                print()
                return
    print("No")
main()
