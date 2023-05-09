def main():
    #input
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #compute
    #dp[i] := the maximum number of stones Takahashi can remove when the pile has i stones.
    dp = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(k):
            if i - a[j] < 0:
                break
            if dp[i - a[j]] == 0:
                dp[i] = 1
                break
    #output
    if dp[n] == 1:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()