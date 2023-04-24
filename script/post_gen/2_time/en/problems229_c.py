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
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= B[i]:
                dp[i+1][w] = max(dp[i][w], dp[i+1][w-B[i]]+A[i])
            else:
                dp[i+1][w] = dp[i][w]
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
    max_a = max(A)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j-B[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])

=======
Suggestion 3

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if max_b > W:
        max_b = W
    max_dp = max_a * max_b
    dp = [0] * (max_dp + 1)
    for i in range(N):
        for j in range(max_dp, 0, -1):
            if j - A[i] * B[i] >= 0:
                dp[j] = max(dp[j], dp[j - A[i] * B[i]] + A[i])
    ans = 0
    for i in range(max_dp + 1):
        if i <= W:
            ans = max(ans, dp[i])
    print(ans)

=======
Suggestion 4

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-B[i]] + A[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[N][W])

=======
Suggestion 5

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j < B[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-B[i]] + A[i])
    print(dp[N][W])

=======
Suggestion 6

def main():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j >= B[i-1]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-B[i-1]]+A[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])

=======
Suggestion 7

def get_input():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, W, A, B

=======
Suggestion 8

def main():
    n, w = map(int, input().split())
    cheese = []
    for i in range(n):
        a, b = map(int, input().split())
        cheese.append((a, b))
    cheese.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        ans += cheese[i][0] * min(cheese[i][1], w)
        w -= min(cheese[i][1], w)
    print(ans)

=======
Suggestion 9

def solve():
    N, W = map(int, input().split())
    items = []
    for i in range(N):
        A, B = map(int, input().split())
        items.append((A, B))

    dp = [0] * (W + 1)
    for i in range(N):
        A, B = items[i]
        for w in range(W, -1, -1):
            if w >= A:
                dp[w] = max(dp[w], dp[w - A] + B)

    print(dp[W])

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0])
    cheese.reverse()
    total = 0
    for c in cheese:
        if W <= 0:
            break
        for _ in range(c[1]):
            if W <= 0:
                break
            total += c[0]
            W -= 1
    print(total)
