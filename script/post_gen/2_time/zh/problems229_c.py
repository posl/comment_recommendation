Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N,W)
    #print(len(A),len(B))
    #print(type(A[0])

=======
Suggestion 2

def main():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(N,W)
    #print(A)
    #print(B)
    #print("------------")
    #dp[i][j]表示前i个物品中总重量为j时的最大价值
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j-B[i-1]>=0:
                dp[i][j] = max(dp[i-1][j-B[i-1]]+A[i-1],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    print(dp[N][W])

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #dp[i][j] 表示前i个物品，重量为j的时候，最大的美味度
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i]*B[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0])
    sum = 0
    for i in range(N):
        if cheese[i][1] >= W:
            sum += cheese[i][0] * W
            break
        else:
            sum += cheese[i][0] * cheese[i][1]
            W -= cheese[i][1]
    print(sum)

=======
Suggestion 5

def max(a, b):
    if a > b:
        return a
    else:
        return b

=======
Suggestion 6

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - B[i] >= 0:
                dp[i + 1][w] = max(dp[i][w], dp[i][w - B[i]] + A[i])
            else:
                dp[i + 1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 7

def main():
    N,W = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N,W)
    #print('-----')
    #dp[i][j]表示前i种奶酪总重量为j时的最大美味值
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j-B[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])

=======
Suggestion 8

def solve():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #dp[i][j]表示：前i种奶酪中，总重量为j时的最大美味值
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    #print(dp)
    print(dp[N][W])

solve()

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0] * w / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j]表示前i种奶酪中，总重量不超过j克的最大美味度
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]] + A[i-1] * B[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])
