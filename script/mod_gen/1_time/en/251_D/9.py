def solve():
    def check():
        for i in range(1, w + 1):
            if dp[i] > 3:
                return False
        return True
    w = int(input())
    dp = [0] * (w + 1)
    for i in range(1, w + 1):
        dp[i] = dp[i - 1] + 1
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i - 3 >= 0:
            dp[i] = min(dp[i], dp[i - 3] + 1)
    if not check():
        print("No")
    else:
        print("Yes")
        for i in range(1, w + 1):
            if dp[i] == 1:
                print(i)
solve()

if __name__ == '__main__':
    solve()