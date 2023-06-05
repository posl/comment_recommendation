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
    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 2

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    #dp[i][j] i:第i种奶酪 j:总重量  dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i]]+a[i])
    dp = [[0]*(w+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j < b[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-b[i-1]]+a[i-1], dp[i-1][j])
    print(dp[n][w])

=======
Suggestion 3

def solve():
    n, w = map(int, input().split())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(w + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + B[i] <= w:
                dp[i + 1][j + B[i]] = max(dp[i + 1][j + B[i]], dp[i][j] + A[i] * B[i])
    print(dp[n][w])


solve()

=======
Suggestion 4

def main():
    n,w = input().split()
    n = int(n)
    w = int(w)
    a = []
    b = []
    for i in range(n):
        ai,bi = input().split()
        a.append(int(ai))
        b.append(int(bi))
    #print(a)
    #print(b)
    ans = 0
    for i in range(n):
        #print(i)
        #print(w)
        #print(a[i])
        #print(b[i])
        if w - a[i] >= 0:
            ans += a[i] * b[i]
            w -= a[i]
        else:
            ans += w * b[i]
            w = 0
        if w == 0:
            break
    print(ans)
main()

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

    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]

    print(dp[N][W])

=======
Suggestion 6

def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0])
    cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]/x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1]/x[0])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]*x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1]*x[0])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]/x[1]*x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1]/x[0]*x[0])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]/x[1]*x[0])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1]/x[0]*x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]/x[1]*x[1]/x[0])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[1]/x[0]*x[0]/x[1])
    # cheese.reverse()
    # print(cheese)
    # print('-----------------------')
    # cheese.sort(key=lambda x: x[0]/x[1]*x[1]/x[

=======
Suggestion 7

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

    #dp = [[0]*(W+1)]*(N+1)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    #print(dp)
    for i in range(N):
        for j in range(W+1):
            if j < B[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j-B[i]] + A[i]*B[i],dp[i][j])
    #print(dp)
    print(dp[N][W])

=======
Suggestion 8

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0]/cheese[i][1]*w
            break
    print(int(ans))

=======
Suggestion 10

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_sum = sum(A)
    dp = [[0 for i in range(max_sum + 1)] for j in range(N + 1)]
    for i in range(N):
        for j in range(max_sum + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    ans = 0
    for i in range(max_sum + 1):
        if dp[N][i] <= W:
            ans = i
    print(ans)

solve()
