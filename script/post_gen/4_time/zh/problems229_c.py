Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for j in range(w + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(w + 1):
            if j >= b[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - b[i]] + a[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][w])

=======
Suggestion 2

def main():
    #读取数据
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)

    #动态规划
    #dp[i][j]表示从前i种奶酪中选出总重量j的最大美味度
    #dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i]]+A[i], dp[i-1][j-2*B[i]]+2*A[i], ...)
    #dp[i][j-B[i]] = max(dp[i-1][j-B[i]], dp[i-1][j-2*B[i]]+A[i], ...)
    #dp[i][j] = max(dp[i-1][j], dp[i][j-B[i]]+A[i])
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
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
    #dp[i][j] 表示前i种奶酪中总量为j时的最大美味度
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j >= b[i]:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-b[i]]+a[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

=======
Suggestion 5

def main():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j-B[i]>=0:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j-B[i]]+A[i])
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
    print(dp[N][W])

=======
Suggestion 6

def get_max_cheese(n, w, cheese_list):
    cheese_list.sort(key=lambda x:x[0]/x[1], reverse=True)
    sum_cheese = 0
    for cheese in cheese_list:
        if cheese[1] < w:
            sum_cheese += cheese[0]
            w -= cheese[1]
        else:
            sum_cheese += cheese[0]/cheese[1]*w
            break
    return sum_cheese

=======
Suggestion 7

def main():
    # 读取数据
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))

    # 从小到大排序
    cheese.sort(key=lambda x: x[0]/x[1])

    # 计算总和
    total = 0
    for i in cheese:
        if w >= i[1]:
            total += i[0]
            w -= i[1]
        else:
            total += i[0] * (w / i[1])
            break

    print(int(total))

=======
Suggestion 8

def solve(n, w, a, b):
    #dp[i][j]表示用了前i种奶酪，总共用了j克奶酪时的美味度
    dp = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j >= b[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i-1]]+a[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]

=======
Suggestion 9

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j] 为前i种奶酪总重量为j时的最大美味度
    dp = [[0 for j in range(W+1)] for i in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

solve()

=======
Suggestion 10

def main():
    import sys
    import math
    import numpy as np
    # 读取输入
    N, W = map(int, sys.stdin.readline().strip().split())
    A = np.zeros(N, dtype=np.int64)
    B = np.zeros(N, dtype=np.int64)
    for i in range(N):
        A[i], B[i] = map(int, sys.stdin.readline().strip().split())
    # 处理
    # 1. 将A和B按照A降序排序
    # 2. 将B/A按照降序排序
    # 3. 从大到小累加B/A，直到W
    # 4. 输出
    # 5. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1
    # 6. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1
    # 7. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1
    # 8. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1，如果W为奇数，且B/A大于1，则将B/A设置为1
    # 9. 优化：从大到小累加B/A，直到W，如果B/A大于1，则将B/A设置为1，如果W为奇数，且B/A小于1，则将B/A设置为1，如果W为
