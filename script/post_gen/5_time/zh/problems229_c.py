Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    N, W = map(int, sys.stdin.readline().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    #print(N, W)
    #dp = [[0 for i in range(W+1)] for j in range(N)]
    dp = [0 for i in range(W+1)]
    for i in range(N):
        for j in range(W, -1, -1):
            if j >= B[i]:
                dp[j] = max(dp[j], dp[j-B[i]] + A[i])
    print(dp[-1])
    #print(dp)

=======
Suggestion 2

def max(a,b):
    if a>=b:
        return a
    else:
        return b

=======
Suggestion 3

def solve():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    #print(a)
    #print(b)
    #dp = [[0 for i in range(w+1)] for j in range(n+1)]
    dp = [0 for i in range(w+1)]
    for i in range(n):
        for j in range(w, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]] + b[i])
    print(dp[w])

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j >= b[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-b[i]]+a[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

=======
Suggestion 5

def main():
    n,w = map(int,input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int,input().split())))
    cheese.sort(key=lambda x:x[0]/x[1],reverse=True)
    ans = 0
    for i in range(n):
        if cheese[i][1] <= w:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0]/cheese[i][1]*w
            break
    print(int(ans))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # dp[i][j] 表示前i个物品中，总重量为j的情况下，总价值最大为多少
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j - a[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]] + b[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][w])

=======
Suggestion 8

def solve():
    N,W = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(N):
        a,b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    maxA = max(A)
    maxB = max(B)
    if maxA > 1000:
        return 0
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j < B[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j-B[i]]+A[i])
    return dp[N][W]

=======
Suggestion 9

def readinput():
    n,w=map(int,input().split())
    ab=[]
    for _ in range(n):
        a,b=map(int,input().split())
        ab.append((a,b))
    return n,w,ab

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    cheese_list = []
    for _ in range(n):
        cheese_list.append(tuple(map(int, input().split())))
    cheese_list.sort(key=lambda x: x[0] / x[1], reverse=True)
    ans = 0
    for cheese in cheese_list:
        if w >= cheese[1]:
            ans += cheese[0]
            w -= cheese[1]
        else:
            ans += cheese[0] * w / cheese[1]
            break
    print(int(ans))
