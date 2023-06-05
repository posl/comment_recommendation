Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N=int(input())
    V=[int(x) for x in input().split()]
    C=[int(x) for x in input().split()]
    X=0
    Y=0
    for i in range(N):
        if V[i]>C[i]:
            X+=V[i]
            Y+=C[i]
    print(X-Y)

=======
Suggestion 2

def solve():
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    max_v = sum(v)
    dp = [[False for i in range(max_v+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(max_v+1):
            if j >= v[i]:
                dp[i+1][j] = dp[i][j-v[i]] or dp[i][j]
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i in range(max_v+1):
        if dp[n][i]:
            ans = max(ans, i-sum(c))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    Vs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    maxvalue = 0
    for i in range(N):
        if Vs[i] - Cs[i] > 0:
            maxvalue += Vs[i] - Cs[i]
    print(maxvalue)
    return

=======
Suggestion 4

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1 << n):
        x = 0
        y = 0
        for j in range(n):
            if i & (1 << j):
                x += v[j]
                y += c[j]
        ans = max(ans, x - y)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 6

def main():
    # N = 3
    # V = [10, 2, 5]
    # C = [6, 3, 4]
    # N = 4
    # V = [13, 21, 6, 19]
    # C = [11, 30, 6, 15]
    # N = 1
    # V = [1]
    # C = [50]
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    print(max(x - y for x, y in zip(V, C) if x > y))

=======
Suggestion 7

def max_value(n, v, c):
    max_value = 0
    for i in range(1, 2**n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += v[j]
                cost += c[j]
        if value > cost and value - cost > max_value:
            max_value = value - cost
    return max_value

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1 << n):
        x = 0
        y = 0
        for j in range(n):
            if (i >> j) & 1:
                x += v[j]
                y += c[j]
        ans = max(ans, x - y)
    print(ans)
main()

=======
Suggestion 9

def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]

    #dp[i][j]表示前i个宝石中，总价值为j时的最小费用
    dp = [[float('inf') for _ in range(10000)] for _ in range(10000)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(10000):
            if j < V[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j - V[i]] + C[i])

    print(max([i for i in range(10000) if dp[N][i] <= i]))

=======
Suggestion 10

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x = 0
    y = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i]
            y += c[i]
    print(x-y)

main()
