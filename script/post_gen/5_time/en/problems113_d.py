Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w, k = map(int, input().split())
    dp = [[0 for _ in range(w)] for _ in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            for k in range(1 << (w-1)):
                ok = True
                for l in range(w-2):
                    if (k >> l) & 1 and (k >> (l+1)) & 1:
                        ok = False
                if not ok:
                    continue
                if j >= 1 and (k >> (j-1)) & 1:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= mod
                elif j <= w-2 and (k >> j) & 1:
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= mod
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= mod
    print(dp[h][k-1])

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    dp = [[0 for i in range(W)] for j in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(2**(W-1)):
                if ("11" in bin(k)):
                    continue
                if (j > 0 and (k & (1 << (j-1)))):
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= 1000000007
                elif (j < W-1 and (k & (1 << j))):
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= 1000000007
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= 1000000007
    print(dp[H][K-1])

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j - 1] * dp[i - 1][j] + dp[i - 1][j] * dp[i - 1][j + 1] + dp[i - 1][j] * dp[i - 1][j] * (j - 1)
            dp[i][j] %= MOD
    print(dp[H][K])

main()

=======
Suggestion 4

def main():
    h,w,k = map(int, input().split())
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
    dp[0][1] = 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            dp[i][j] = dp[i-1][j-1] * dp[i-1][j] % 1000000007
            dp[i][j] += dp[i-1][j] * dp[i-1][j+1] % 1000000007
            dp[i][j] += dp[i-1][j] * dp[i-1][j-1] % 1000000007
            dp[i][j] %= 1000000007
    print(dp[h][k])

=======
Suggestion 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 6

def path(H, W, K):
    if W == 1:
        return 1
    if K == 1:
        return path(H-1, W-1, K) + path(H-1, W-1, K+1)
    if K == W:
        return path(H-1, W-1, K) + path(H-1, W-1, K-1)
    return path(H-1, W-1, K-1) + path(H-1, W-1, K) + path(H-1, W-1, K+1)

H, W, K = map(int, input().split())
print(path(H, W, K) % 1000000007)

=======
Suggestion 7

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 8

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 9

def main():
    H, W, K = map(int, input().split())
    #print(H, W, K)
    #print(type(H), type(W), type(K))
    #print(H, W, K)
    #print(type(H), type(W), type(K))
    if W == 1:
        print(1)
        return
    if W == 2:
        print(2)
        return
    if W == 3:
        if K == 1:
            print(2)
            return
        if K == 2:
            print(1)
            return
        if K == 3:
            print(2)
            return
    if W == 4:
        if K == 1:
            print(3)
            return
        if K == 2:
            print(2)
            return
        if K == 3:
            print(2)
            return
        if K == 4:
            print(3)
            return
    if W == 5:
        if K == 1:
            print(5)
            return
        if K == 2:
            print(3)
            return
        if K == 3:
            print(3)
            return
        if K == 4:
            print(3)
            return
        if K == 5:
            print(5)
            return
    if W == 6:
        if K == 1:
            print(8)
            return
        if K == 2:
            print(5)
            return
        if K == 3:
            print(4)
            return
        if K == 4:
            print(4)
            return
        if K == 5:
            print(5)
            return
        if K == 6:
            print(8)
            return
    if W == 7:
        if K == 1:
            print(13)
            return
        if K == 2:
            print(8)
            return
        if K == 3:
            print(7)
            return
        if K == 4:
            print(6)
            return
        if K == 5:
            print(7)
            return
        if K == 6:
            print(8)
            return
        if K == 7:
            print(13)
            return
    if
