Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j]表示前i种奶酪中取总重量不超过j的最大美味度
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

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
    # print('N =', N)
    # print('W =', W)
    # print('A =', A)
    # print('B =', B)
    # print('N =', N)
    # print('W =', W)
    # print('A =', A)
    # print('B =', B)

    # dp[i][w] := 使用前i种奶酪，总重量为w时的美味度
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - B[i] >= 0:
                dp[i + 1][w] = max(dp[i][w], dp[i][w - B[i]] + A[i])
            else:
                dp[i + 1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    #print(n, w)
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    dp = [0 for i in range(w+1)]
    for i in range(n):
        for j in range(w, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]]+b[i])
    print(dp[w])
main()

=======
Suggestion 4

def get_max_cheese(n, w, cheese):
    cheese = sorted(cheese, key=lambda x: x[0] / x[1], reverse=True)
    sum = 0
    for i in range(n):
        if w >= cheese[i][1]:
            w -= cheese[i][1]
            sum += cheese[i][0]
        else:
            sum += cheese[i][0] * w / cheese[i][1]
            break
    return sum

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    max_a = max(A)
    max_b = max(B)
    if max_a > 1000 or max_b > 1000:
        return
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0] / x[1], reverse=True)
    ans = 0
    for i in range(N):
        if W >= cheese[i][1]:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 7

def get_input():
    n, w = map(int, input().split())
    cheese = []
    for _ in range(n):
        cheese.append(list(map(int, input().split())))
    return n, w, cheese

=======
Suggestion 8

def problems229_c():
    return 0

=======
Suggestion 9

def solve():
    N, W = [int(x) for x in input().split()]
    A = []
    B = []
    for i in range(N):
        a, b = [int(x) for x in input().split()]
        A.append(a)
        B.append(b)
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 10

def solve():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for w in range(1,W+1):
            if w >= B[i-1]:
                dp[i][w] = max(dp[i-1][w-B[i-1]]+A[i-1],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    print(dp[N][W])
