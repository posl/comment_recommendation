Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    max_value = 0
    for i in range(1 << n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += V[j]
                cost += C[j]
        max_value = max(max_value, value - cost)
    print(max_value)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[0 for _ in range(101)] for _ in range(n+1)]

    for i in range(n):
        for j in range(101):
            if j < c[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]]+v[i])

    print(dp[n][100])

=======
Suggestion 3

def get_max_value(n, v, c):
    dp = [[0 for _ in range(10000)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(10000):
            if j < c[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - c[i]] + v[i])
    return dp[n][9999]

=======
Suggestion 4

def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
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

=======
Suggestion 5

def get_max_profit(N, V, C):
    max_profit = 0
    for i in range(2**N):
        profit = 0
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                profit += V[j]
                cost += C[j]
        if profit - cost > max_profit:
            max_profit = profit - cost
    return max_profit

=======
Suggestion 6

def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    #print(n,v,c)
    v_sum = 0
    c_sum = 0
    for i in range(n):
        v_sum += v[i]
        c_sum += c[i]
    #print(v_sum,c_sum)
    print(v_sum - c_sum)

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    max_value = 0
    for i in range(1 << n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += v[j]
                cost += c[j]
        max_value = max(max_value, value - cost)
    print(max_value)

=======
Suggestion 8

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max_diff = 0
    for i in range(N):
        if V[i] > C[i]:
            max_diff += V[i] - C[i]
    print(max_diff)

=======
Suggestion 9

def problems125_b():
    pass

=======
Suggestion 10

def main():
    n = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)
