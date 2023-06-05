Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, k, v):
    res = 0
    for i in range(min(k, n) + 1):
        for j in range(min(k - i, n - i) + 1):
            l = v[:i] + v[n - j:]
            res = max(res, sum(l))
    return res

n, k = map(int, input().split())
v = list(map(int, input().split()))
print(solve(n, k, v))

=======
Suggestion 2

def max_sum(N,K,V):
    if K >= N:
        return sum(V)
    else:
        max_sum = 0
        for i in range(K+1):
            for j in range(i+1):
                sum_left = sum(V[:j])
                sum_right = sum(V[N-(i-j):])
                if sum_left + sum_right > max_sum:
                    max_sum = sum_left + sum_right
        return max_sum

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if i+j > k:
                continue
            r = k - i - j
            t = []
            for l in range(i):
                t.append(v[l])
            for l in range(n-j,n):
                t.append(v[l])
            t.sort()
            for l in range(r):
                if len(t) == 0:
                    break
                if t[0] > 0:
                    break
                t.pop(0)
            ans = max(ans,sum(t))
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K+1):
        for l in range(i+1):
            r = i - l
            now = V[:l] + V[N-r:]
            now.sort()
            now = sum(now[max(0, len(now)-K):])
            ans = max(ans, now)
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for l in range(min(n,k)+1):
        for r in range(min(n,k)-l+1):
            if l+r > n:
                continue
            t = []
            for i in range(l):
                t.append(v[i])
            for i in range(n-r,n):
                t.append(v[i])
            t.sort()
            s = 0
            for i in range(len(t)):
                if t[i] < 0 and i < k-l-r:
                    continue
                s += t[i]
            ans = max(ans,s)
    print(ans)

=======
Suggestion 7

def solve(n, k, v):
    ans = 0
    for i in range(0, min(n+1, k+1)):
        for j in range(0, min(n+1, k+1)):
            if i+j > k:
                continue
            l = i
            r = n - j
            a = v[:l] + v[r:]
            a.sort()
            ans = max(ans, sum(a[j:]))
    return ans

n, k = list(map(int, input().split()))
v = list(map(int, input().split()))
print(solve(n, k, v))

=======
Suggestion 8

def solve(n, k, v):
    ans = 0
    for i in range(0, k+1):
        for j in range(0, k+1):
            if i+j > n:
                continue
            dp = [[0 for x in range(n+1)] for y in range(k+1)]
            for l in range(0, k+1):
                for m in range(0, n+1):
                    if l == 0 and m == 0:
                        continue
                    dp[l][m] = -float('inf')
                    if m > 0 and l > 0:
                        dp[l][m] = max(dp[l][m], dp[l-1][m-1] + v[i+l-1])
                    if m > 0 and i+j-l > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1] + v[i+j-l-1])
                    if m > 0 and j > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1])
                    if m > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1])
                    if l > 0:
                        dp[l][m] = max(dp[l][m], dp[l-1][m])
            ans = max(ans, dp[k][n])
    return ans

=======
Suggestion 9

def max_sum(N, K, V):
    max_sum = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if K >= (j-i):
                sum = 0
                for k in range(i, j):
                    sum += V[k]
                max_sum = max(max_sum, sum)
    return max_sum

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    if K > N:
        K = N
    max_sum = 0
    for i in range(K+1):
        for j in range(K+1-i):
            sum = 0
            left = V[:i]
            right = V[N-j:]
            sum = sum + sum(left) + sum(right)
            left.sort()
            right.sort()
            for k in range(min(i, j)):
                if left[k] < right[-1-k]:
                    sum = sum - left[k] + right[-1-k]
            max_sum = max(max_sum, sum)
    print(max_sum)
