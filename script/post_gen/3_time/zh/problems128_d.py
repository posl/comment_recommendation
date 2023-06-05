Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n,k,v):
    dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+v[i-1])
            dp[i][j][1] = max(dp[i-1][j-1][1],dp[i-1][j-1][0]-v[i-1])
    return dp[n][k][0]

n,k = map(int,input().split())
v = list(map(int,input().split()))
print(solve(n,k,v))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))

    # dp[i][j][l]表示前i个珠宝，操作j次，手中有l个珠宝时的最大值
    dp = [[[float('-inf') for _ in range(n+1)] for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0] = 0

    for i in range(1, n+1):
        for j in range(k+1):
            for l in range(n+1):
                # 操作A
                if l >= 1:
                    dp[i][j][l] = dp[i-1][j][l-1]
                # 操作B
                if l < n:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l+1])
                # 操作C
                if j >= 1:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l] + values[i-1])
                # 操作D
                if j >= 1 and l < n:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l+1] + values[i-1])
    ans = 0
    for j in range(k+1):
        for l in range(n+1):
            ans = max(ans, dp[n][j][l])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    # print(N, K, V)
    max_sum = 0
    for i in range(K+1):
        for j in range(K+1-i):
            if i+j > N:
                continue
            # print(i, j, N-i-j)
            # print(V[:i])
            # print(V[N-j:])
            sum = 0
            if i > 0:
                sum += sum(V[:i])
            if j > 0:
                sum += sum(V[N-j:])
            if sum > max_sum:
                max_sum = sum
    print(max_sum)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1):
            if i + j > min(n, k):
                continue
            l = i
            r = k - i - j
            now = 0
            cur = v[:]
            for _ in range(l):
                now += cur.pop(0)
            for _ in range(r):
                now += cur.pop()
            cur.sort()
            for _ in range(j):
                if cur[-1] < 0:
                    cur.pop()
                else:
                    break
            now += sum(cur)
            ans = max(ans, now)
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1 - l):
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(N - r, N):
                tmp.append(V[i])
            tmp.sort()
            for i in range(K - l - r):
                if i >= len(tmp):
                    break
                if tmp[i] < 0:
                    tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)
solve()

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k)+1):
        for j in range(min(n, k)-i+1):
            a = v[:i] + v[n-j:]
            a.sort(reverse=True)
            ans = max(ans, sum(a))
    print(ans)

=======
Suggestion 7

def main():
    print("")

=======
Suggestion 8

def problems128_d():
    return None

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for left in range(0, min(K+1, N+1)):
        for right in range(0, min(K+1-left, N+1)):
            now = V[:left] + V[N-right:]
            now.sort()
            ans = max(ans, sum(now[max(0, K-left-right):]))
    print(ans)
