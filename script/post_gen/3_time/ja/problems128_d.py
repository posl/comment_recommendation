Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            arr = V[:i] + V[N - j:]
            arr.sort()
            tmp = 0
            for k in range(min(K - i - j, len(arr))):
                if arr[k] < 0:
                    arr[k] = 0
            tmp = sum(arr)
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
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
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) + 1 - l):
            dp = [0] * (N + 1)
            for i in range(l):
                dp[i + 1] = dp[i] + V[i]
            for i in range(r):
                dp[N - i - 1] = dp[N - i] + V[N - i - 1]
            dp[l + r] = dp[l] + dp[N - r]
            dp[l + r] += sum(sorted(V)[N - l - r:N - r])
            ans = max(ans, dp[l + r])
    print(ans)

=======
Suggestion 4

def main():
    n,k=map(int,input().split())
    v=list(map(int,input().split()))
    ans=0
    for i in range(min(n,k)+1):
        for j in range(min(n,k)-i+1):
            w=v[:i]+v[n-j:]
            w.sort()
            for l in range(min(len(w),k-i-j)):
                if w[l]<0:
                    w[l]=0
            ans=max(ans,sum(w))
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(0, min(N, K) + 1):
        for r in range(0, min(N, K) - l + 1):
            if l + r > N or l + r > K:
                continue
            d = V[:l] + V[N - r:]
            d.sort()
            for i in range(min(K - l - r, len(d))):
                if d[i] < 0:
                    d[i] = 0
            ans = max(ans, sum(d))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for l in range(min(N,K)+1):
        for r in range(min(N,K)-l+1):
            hand = V[:l] + V[N-r:]
            hand.sort()
            for i in range(K-l-r):
                if hand and hand[0] < 0:
                    hand.pop(0)
                else:
                    break
            ans = max(ans, sum(hand))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    for i in range(1, min(N, K)+1):
        for j in range(i+1):
            tmp = V[:j] + V[N-(i-j):]
            tmp.sort()
            s = sum(tmp)
            for k in range(min(K-i, i-j)):
                if tmp[k] >= 0:
                    break
                s -= tmp[k]
            ans = max(ans, s)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for i in range(min(N+1, K+1)):
        for j in range(min(N+1, K+1)-i):
            values = []
            for k in range(i):
                values.append(V[k])
            for k in range(j):
                values.append(V[N-1-k])
            values.sort()
            for k in range(min(K-i-j, len(values))):
                if values[k] < 0:
                    values[k] = 0
            max_value = max(max_value, sum(values))
    print(max_value)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(0, min(n, k)+1):
        for l in range(0, min(n, k)-i+1):
            r = k - i - l
            tmp = v[:i] + v[n-l:]
            tmp.sort()
            for j in range(min(r, len(tmp))):
                if tmp[j] < 0:
                    tmp[j] = 0
            ans = max(ans, sum(tmp))
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    V.reverse()
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K, N) - i + 1):
            d = V[:i] + V[N - j:]
            d.sort()
            for k in range(min(K - i - j, len(d))):
                if d[k] < 0:
                    d[k] = 0
            ans = max(ans, sum(d))
    print(ans)
