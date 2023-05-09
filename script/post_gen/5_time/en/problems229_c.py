Synthesizing 10/10 solutions

=======
Suggestion 1

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
    #print(N, W)
    dp = [[0 for i in range(3*10**5+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(3*10**5+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    ans = 0
    for i in range(3*10**5+1):
        if i <= W:
            ans = max(ans, dp[N][i])
    print(ans)

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
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= B[i]:
                dp[i+1][w] = max(dp[i][w], dp[i][w-B[i]]+A[i])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # dp[i][j]: i番目までの品物から重さがj以下になるように選んだときの価値の総和の最大値
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(W + 1):
            if j >= A[i]:
                dp[i + 1][j] = max(dp[i][j - A[i]] + B[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]

    print(dp[N][W])

=======
Suggestion 5

def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w, 0, -1):
            if j >= b[i]:
                dp[j] = max(dp[j], dp[j - b[i]] + a[i])
    print(dp[w])

=======
Suggestion 6

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
            if j < b[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-b[i]]+a[i]*b[i])
    print(dp[n][w])

=======
Suggestion 7

def main():
    #N, W = map(int, input().split())
    #A = []
    #B = []
    #for i in range(N):
    #    a, b = map(int, input().split())
    #    A.append(a)
    #    B.append(b)
    N, W = map(int, "10 3141".split())
    A = list(map(int, "314944731 140276783 578012421 878510647 925326537 337666726 879137070 87808915 756059990 228622672".split()))
    B = list(map(int, "649 228 809 519 943 611 306 39 244 291".split()))
    #N, W = map(int, "3 5".split())
    #A = list(map(int, "3 4 2".split()))
    #B = list(map(int, "1 2 3".split()))
    #N, W = map(int, "4 100".split())
    #A = list(map(int, "6 1 3 8".split()))
    #B = list(map(int, "2 5 9 7".split()))
    #N, W = map(int, "10 3141".split())
    #A = list(map(int, "314944731 140276783 578012421 878510647 925326537 337666726 879137070 87808915 756059990 228622672".split()))
    #B = list(map(int, "649 228 809 519 943 611 306 39 244 291".split()))
    #N, W = map(int, "3 5".split())
    #A = list(map(int, "3 4 2".split()))
    #B = list(map(int, "1 2 3".split()))
    #N, W = map(int, "4 100".split())
    #A = list(map(int, "6 1 3 8".split()))
    #B = list(map(int, "2 5 9 7".split()))
    #N, W = map(int, "10 3141".split())
    #A = list(map(int, "314944731 140276783 578012

=======
Suggestion 8

def main():
    n, w = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(n):
        a_i, b_i = [int(x) for x in input().split()]
        a.append(a_i)
        b.append(b_i)

    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(w+1):
            if j >= b[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i-1]]+a[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][w])

=======
Suggestion 9

def main():
    # Get input here
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        a, b = map(int, input().split())
        cheese.append((a, b))
    # Solve problems
    # Sort cheese by deliciousness
    cheese.sort(key=lambda x: x[0])
    # print(cheese)
    # dp[i][j]: Max deliciousness using i items and j grams of cheese
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            if j - cheese[i - 1][1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cheese[i - 1][1]] + cheese[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]
    # print(dp)
    # Get output here
    print(dp[N][W])

=======
Suggestion 10

def max_deliciousness(N, W, A, B):
    #print("N: ", N, "W: ", W, "A: ", A, "B:", B)
    #print("max(A): ", max(A), "max(B): ", max(B))
    #print("sum(B): ", sum(B))
    #print("sum(A): ", sum(A))
    #print("W: ", W)
    if sum(B) <= W:
        return sum(A)
    else:
        max_del = 0
        for i in range(N):
            max_del += (A[i] * min(B[i], W))
            W -= min(B[i], W)
            if W == 0:
                break
        return max_del
