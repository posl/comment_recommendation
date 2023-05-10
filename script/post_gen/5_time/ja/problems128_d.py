Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            gems = V[:l] + V[N - r:]
            gems.sort()
            tmp = sum(gems)
            for i in range(min(K - l - r, l + r)):
                if gems[i] < 0:
                    tmp -= gems[i]
            ans = max(ans, tmp)

    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(N+1):
        for r in range(N+1):
            if l + r > K:
                continue
            if l + r > N:
                continue
            if l + r == 0:
                continue
            if l + r == K:
                ans = max(ans, sum(V))
                continue
            v = V[:l] + V[N-r:]
            v.sort()
            for i in range(min(K - (l+r), len(v))):
                if v[i] >= 0:
                    break
                v[i] = 0
            ans = max(ans, sum(v))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1):
            if l + r > min(K, N):
                continue
            if l + r > N:
                continue
            if l + r > K:
                continue

            # print(l, r)

            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])

            tmp.sort()

            # print(tmp)

            for i in range(min(K - l - r, len(tmp))):
                if tmp[i] < 0:
                    tmp[i] = 0

            # print(tmp)

            ans = max(ans, sum(tmp))

    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                continue
            if l + r > K:
                continue
            if l + r == 0:
                continue
            V2 = sorted(V[:l] + V[N-r:])
            #print(V2)
            tmp = sum(V2)
            for i in range(min(K-l-r, len(V2))):
                if V2[i] < 0:
                    tmp -= V2[i]
                else:
                    break
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1 - i):
            temp = V[:i] + V[N - j:]
            temp.sort()
            ans = max(ans, sum(temp[K - i - j:]))
    print(ans)

=======
Suggestion 6

def max_value(n, k, v):
    #dp[i][j][0] = i回操作して、j個残っているときに、左端をとったときの最大価値
    #dp[i][j][1] = i回操作して、j個残っているときに、右端をとったときの最大価値
    dp = [[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(k+1)]
    for i in range(k):
        for j in range(n+1):
            if j == 0:
                dp[i+1][j][0] = dp[i][j][0]
                dp[i+1][j][1] = dp[i][j][1]
            else:
                dp[i+1][j][0] = max(dp[i][j][0]+v[j-1], dp[i][j][0])
                dp[i+1][j][1] = max(dp[i][j][1]+v[n-j], dp[i][j][1])
                if i > 0:
                    dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j-1][1]+v[j-1])
                    dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j-1][0]+v[n-j])
    return max(dp[k][n][0], dp[k][n][1])

n, k = map(int, input().split())
v = list(map(int, input().split()))
print(max_value(n, k, v))

=======
Suggestion 7

def problem128_d():
    n, k = map(int, input().split())
    vs = list(map(int, input().split()))

    ans = 0
    for l in range(min(n, k) + 1):
        for r in range(min(n, k) - l + 1):
            if l + r > k:
                continue
            values = vs[:l] + vs[n-r:]
            values.sort()
            for v in values[:k - l - r]:
                if v < 0:
                    values.remove(v)
            ans = max(ans, sum(values))

    print(ans)

=======
Suggestion 8

def solve(N, K, V):
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            tmp = []
            for k in range(i):
                tmp.append(V[k])
            for k in range(j):
                tmp.append(V[N - 1 - k])
            tmp.sort()
            for k in range(min(K - i - j, len(tmp))):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    return ans

N, K = map(int, input().split())
V = list(map(int, input().split()))
print(solve(N, K, V))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N or l + r > K:
                continue
            if l + r == 0:
                continue
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])
            tmp.sort()
            cnt = K - l - r
            for i in range(min(cnt, len(tmp))):
                if tmp[i] < 0:
                    tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            bag = V[:i] + V[N-j:]
            bag.sort()
            for k in range(min(K - i - j, len(bag))):
                if bag[k] < 0:
                    bag[k] = 0
            ans = max(ans, sum(bag))
    print(ans)
