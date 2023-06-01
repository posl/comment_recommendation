Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_value(n, values, costs):
    max_value = 0
    for i in range(2**n):
        value = 0
        cost = 0
        for j in range(n):
            if i & (1 << j):
                value += values[j]
                cost += costs[j]
        if value - cost > max_value:
            max_value = value - cost
    return max_value

=======
Suggestion 2

def solve(n,v,c):
    dp = [[0]*(n+1) for _ in range(51)]
    for i in range(1,n+1):
        for j in range(51):
            if j < c[i-1]:
                dp[j][i] = dp[j][i-1]
            else:
                dp[j][i] = max(dp[j][i-1],dp[j-c[i-1]][i-1]+v[i-1])
    return dp[50][n]

n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
print(solve(n,v,c))

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1<<n):
        x = 0
        y = 0
        for j in range(n):
            if (i>>j)&1:
                x += v[j]
                y += c[j]
        ans = max(ans, x-y)
    print(ans)

=======
Suggestion 4

def get_list():
    n = int(input())
    v_list = list(map(int,input().split()))
    c_list = list(map(int,input().split()))
    return n,v_list,c_list

=======
Suggestion 5

def solve():
    # 读入数据
    N = int(input())
    V = [int(item) for item in input().split()]
    C = [int(item) for item in input().split()]
    # 初始化dp
    dp = [[0 for i in range(51)] for j in range(51)]
    # 状态转移
    for i in range(N):
        for j in range(51):
            if j < C[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - C[i]] + V[i])
    # 打印结果
    print(dp[N][50])
solve()

=======
Suggestion 6

def value_of_gems(N, V, C):
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    return X - Y

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
print(value_of_gems(N, V, C))

=======
Suggestion 7

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1<<n):
        x = 0
        y = 0
        for j in range(n):
            if i & (1<<j):
                x += v[j]
                y += c[j]
        ans = max(ans, x-y)
    print(ans)

solve()

=======
Suggestion 8

def max_value(N, V, C):
    max_diff = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = V[i] - C[j]
            if diff > max_diff:
                max_diff = diff
    return max_diff

=======
Suggestion 9

def solve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

solve()

=======
Suggestion 10

def f(n, v, c):
    dp = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in range(n):
        for j in range(1000):
            if j < c[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]] + v[i])
    return dp[n][999]

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
print(f(n, v, c))
