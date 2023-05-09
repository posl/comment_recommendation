def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (n+1)
    for i in range(1, n+1):
        for j in range(k):
            if i - a[j] >= 0 and dp[i-a[j]] == False:
                dp[i] = True
    for i in range(n, 0, -1):
        if dp[i] == False:
            print(i)
            exit()

if __name__ == '__main__':
    solve()