def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n+1)
    for i in range(n):
        if dp[i] == 0:
            for j in a:
                if i+j <= n:
                    dp[i+j] = 1
    if dp[n] == 1:
        print("First")
    else:
        print("Second")
main()
