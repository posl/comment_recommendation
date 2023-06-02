Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, k, v):
    dp = [[[0 for i in range(n+1)] for j in range(n+1)] for l in range(k+1)]
    for i in range(1, k+1):
        for j in range(n+1):
            for l in range(n+1):
                if j > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l]+v[j-1])
                if l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l-1])
                if j > 0 and l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l-1])
    return dp[k][n][n]

=======
Suggestion 2

def max_value(N, K, V):
    max_sum = 0
    for i in range(0, min(K, N) + 1):
        for j in range(0, min(K - i, N - i) + 1):
            if i + j > N:
                continue
            else:
                sum = 0
                sum += sum_max(V[0:i])
                sum += sum_max(V[N - j:N])
                max_sum = max(max_sum, sum)
    return max_sum

=======
Suggestion 3

def dp(n, k, v):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i+1][j] = dp[i][j] + v[i]
            else:
                dp[i+1][j] = max(dp[i][j] + v[i], dp[i][j-1])
    return dp[n][k]

n, k = map(int, input().split())
v = list(map(int, input().split()))
print(dp(n, k, v))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            # print(i, j)
            # print(V[:i] + V[N-j:])
            ans = max(ans, sum(sorted(V[:i] + V[N-j:])[j:]))
    print(ans)

=======
Suggestion 6

def max_sum(N, K, V):
    if K == 0:
        return 0
    if N == 1:
        return V[0]
    if N == 2:
        return max(V[0], V[1])
    if N == 3:
        return max(V[0] + V[2], V[1])
    if N == 4:
        return max(V[0] + V[2], V[1] + V[3])
    if N == 5:
        return max(V[0] + V[2] + V[4], V[1] + V[3])
    if N == 6:
        return max(V[0] + V[2] + V[4], V[1] + V[3] + V[5])

=======
Suggestion 7

def solve():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(min(N,K)+1):
        for j in range(min(N-i,K-i)+1):
            #print(i,j)
            v = V[:i]+V[N-j:]
            v.sort()
            for k in range(K-i-j):
                if k < len(v) and v[k] < 0:
                    v[k] = 0
            ans = max(ans,sum(v))
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(K+1):
        for b in range(K+1-a):
            c = K-a-b
            l = sorted([V[i] for i in range(a)])
            r = sorted([V[i] for i in range(N-b, N)], reverse=True)
            s = sum(l)+sum(r)
            for _ in range(min(c, len(l), len(r))):
                if l[_] < r[_]:
                    s += r[_]-l[_]
                else:
                    break
            ans = max(ans, s)
    print(ans)

solve()

=======
Suggestion 9

def max_sum(N, K, V):
    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            left = V[:i]
            right = V[N-j:]
            left.sort()
            right.sort()
            ans = max(ans, sum(right)-sum(left))
    return ans
