Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K)+1):
        for r in range(min(N, K)-l+1):
            a = V[:l]
            b = V[N-r:]
            c = V[l:N-r]
            for i in range(min(K-l-r, min(l, r))):
                if a[i] < b[i]:
                    a[i], b[i] = b[i], a[i]
            a.sort()
            b.sort(reverse=True)
            for i in range(min(K-l-r, len(c))):
                if c[i] < b[i]:
                    c[i], b[i] = b[i], c[i]
            ans = max(ans, sum(a)+sum(b))
    print(ans)

solve()

=======
Suggestion 2

def solve(n, k, v):
    ans = 0
    for i in range(1, k+1):
        for j in range(i+1):
            if j <= n and i-j <= n:
                dp = [[-10**9 for _ in range(i+1)] for _ in range(i+1)]
                dp[0][0] = 0
                for l in range(n):
                    if l != j-1 and l != n-(i-j):
                        for m in range(i+1):
                            if m != 0:
                                dp[l+1][m] = max(dp[l+1][m], dp[l][m-1]+v[l])
                            dp[l+1][m] = max(dp[l+1][m], dp[l][m])
                ans = max(ans, dp[n][i-j])
    return ans

n, k = map(int, input().split())
v = list(map(int, input().split()))
print(solve(n, k, v))

=======
Suggestion 3

def problems128_d():
    pass

=======
Suggestion 4

def solve(N, K, V):
    # dp[i][j][k]表示第i次操作后，左端有j个宝石，右端有k个宝石时的最大值
    dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(K+1)]
    for i in range(N):
        dp[0][0][i] = V[i]

    for i in range(1, K+1):
        for j in range(N+1):
            for k in range(N+1):
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+V[j-1])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+V[N-k])
                if j < N:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j+1][k])
                if k < N:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k+1])
    return dp[K][0][0]

=======
Suggestion 5

def problems128_d():
    return None

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1 - l):
            a = V[:l] + V[N - r:]
            a.sort()
            ans = max(ans, sum(a[max(0, K - l - r):]))
    print(ans)

main()

=======
Suggestion 7

def get_max_value(n,k,v):
    if n==1:
        return v[0]
    if k==0:
        return 0
    max_value = 0
    for i in range(0,n):
        for j in range(i+1,n+1):
            value = get_max_value(i,k-1,v[0:i]) + get_max_value(j-i,k-1,v[i:j]) + get_max_value(n-j,k-1,v[j:n])
            if value > max_value:
                max_value = value
    return max_value

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) - i + 1):
            tmp = v[:i] + v[n - j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, k - i - j):]))
    print(ans)

=======
Suggestion 9

def solve(n, k, v):
    result = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1 - i):
            l = max(0, i - n)
            r = max(0, j - n)
            dp = [[0] * (n + l + r + 1) for _ in range(n + 1)]
            for x in range(n + 1):
                for y in range(n + l + r + 1):
                    dp[x][y] = -float('inf')
                dp[x][0] = 0
            for x in range(n):
                for y in range(n + l + r + 1):
                    dp[x + 1][y] = max(dp[x + 1][y], dp[x][y])
                    if y + 1 < n + l + r + 1:
                        dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y] + v[x])
            result = max(result, dp[n][i + j + l])
    print(result)
    return result

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K)+1):
        for r in range(min(N, K)-l+1):
            now = 0
            Vl = V[:l]
            Vr = V[N-r:]
            Vl.sort()
            Vr.sort()
            for i in range(K-l-r):
                if i < len(Vl) and Vl[i] < 0:
                    Vl[i] = 0
                if i < len(Vr) and Vr[i] < 0:
                    Vr[i] = 0
            now += sum(Vl) + sum(Vr)
            Vl.sort(reverse=True)
            Vr.sort(reverse=True)
            for i in range(min(K-l-r, len(Vl))):
                now -= Vl[i]
            for i in range(min(K-l-r, len(Vr))):
                now -= Vr[i]
            ans = max(ans, now)
    print(ans)
solve()
