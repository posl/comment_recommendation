Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[0 for _ in range(1001)] for _ in range(1001)]

    for i in range(n):
        for j in range(1000, -1, -1):
            if j >= c[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[n][1000])

=======
Suggestion 2

def solve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            sum += v[i] - c[i]
    print(sum)

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

    x = 0
    y = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i]
            y += c[i]

    print(x - y)

=======
Suggestion 6

def main():
    n = int(input())
    v = [int(x) for x in input().split(' ')]
    c = [int(x) for x in input().split(' ')]
    res = 0
    for i in range(1 << n):
        s1, s2 = 0, 0
        for j in range(n):
            if (i >> j) & 1:
                s1 += v[j]
                s2 += c[j]
        res = max(res, s1 - s2)
    print(res)

=======
Suggestion 7

def max_value(N, V, C):
    # 递归
    # if N == 0:
    #     return 0
    # elif V[N-1] < C[N-1]:
    #     return max_value(N-1, V, C)
    # else:
    #     return max(max_value(N-1, V, C), max_value(N-1, V, C))

    # 动态规划
    dp = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(N):
        for j in range(1000):
            if j < C[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-C[i]]+V[i])
    return dp[N][999]

=======
Suggestion 8

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    max = 0
    for i in range(1, 2**n):
        sum_v = 0
        sum_c = 0
        for j in range(n):
            if (i >> j) & 1:
                sum_v += v[j]
                sum_c += c[j]
        if sum_v - sum_c > max:
            max = sum_v - sum_c
    print(max)

=======
Suggestion 9

def get_max_profit(N, Vs, Cs):
    max_profit = 0
    for i in range(1 << N):
        profit = 0
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                profit += Vs[j]
                cost += Cs[j]
        if profit > cost and profit - cost > max_profit:
            max_profit = profit - cost
    return max_profit
