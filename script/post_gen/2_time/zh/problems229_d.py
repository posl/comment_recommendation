Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))
    cheese = sorted(cheese, key=lambda x: x[0] / x[1])
    cheese = cheese[::-1]
    ans = 0
    for i in range(n):
        if w <= 0:
            break
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0] * w / cheese[i][1]
            w = 0
    print(int(ans))

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #dp[i][w]表示前i个物品中总重量不超过w时的最大价值
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= B[i]:
                dp[i+1][w] = max(dp[i][w], dp[i+1][w-B[i]]+A[i])
            else:
                dp[i+1][w] = dp[i][w]
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
    max_a = max(A)
    max_b = max(B)
    if (max_a * max_b * N) < W:
        print(sum(A) * sum(B))
        return
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j >= B[i]:
                dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

=======
Suggestion 4

def get_input():
    N, W = input().split()
    N = int(N)
    W = int(W)
    A = []
    B = []
    for i in range(N):
        a, b = input().split()
        A.append(int(a))
        B.append(int(b))
    return N, W, A, B

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]] + A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #dp[i][j]表示前i种奶酪中总重量为j时的最大美味度
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j-B[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][W])

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, B[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(N)
    # print(W)
    # print(len(A))
    # print(len(B))
    # print(A[0])
    # print(B[0])

    # print(A[0] * B[0])
    # print(A[1] * B[1])
    # print(A[2] * B[2])
    # print(A[3] * B[3])
    # print(A[4] * B[4])
    # print(A[5] * B[5])
    # print(A[6] * B[6])
    # print(A[7] * B[7])
    # print(A[8] * B[8])
    # print(A[9] * B[9])
    # print(A[10] * B[10])
    # print(A[11] * B[11])
    # print(A[12] * B[12])
    # print(A[13] * B[13])
    # print(A[14] * B[14])
    # print(A[15] * B[15])
    # print(A[16] * B[16])
    # print(A[17] * B[17])
    # print(A[18] * B[18])
    # print(A[19] * B[19])
    # print(A[20] * B[20])
    # print(A[21] * B[21])
    # print(A[22] * B[22])
    # print(A[23] * B[23])
    # print(A[24] * B[24])
    # print(A[25] * B[25])
    # print(A[26] * B[26])
    # print(A[27] * B[27])
    # print(A[28] * B[28])
    # print(A[29] * B[29])
    # print(A[30] * B[30])
    # print(A[31] * B[31])
    # print(A[32] * B[32])
    # print(A[33]

=======
Suggestion 9

def solve(N, W, A, B):
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            if j < B[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]] + A[i-1])
    return dp[N][W]

=======
Suggestion 10

def main():
    N,W = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #print(N,W,A,B)

    #dp[i][j]表示使用前i种奶酪，总重量为j时的最大美味值
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(W+1):
            if j < B[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-B[i-1]]+A[i-1]*B[i-1])
    #print(dp)
    print(dp[N][W])
