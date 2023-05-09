Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(1, i - R[j])
            r = max(0, i - L[j])
            if r < l:
                continue
            dp[i] += dpsum[r] - dpsum[l - 1]
        dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
    print(dp[N])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    mod = 998244353
    dp = [0]*(N+1)
    dp[1] = 1
    dpsum = [0]*(N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            if i-L[j] < 1:
                continue
            dp[i] += dpsum[i-L[j]] - dpsum[max(i-R[j]-1, 0)]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[N])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            l = max(0, i-R[j])
            r = max(0, i-L[j]+1)
            dp[i] += (dpsum[r] - dpsum[l]) % MOD
        dpsum[i] = dpsum[i-1] + dp[i]
    print(dp[N] % MOD)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * N
    dpsum[0] = 1
    for i in range(1, N):
        for j in range(K):
            if i - L[j] >= 0:
                dp[i] += dpsum[i - L[j]]
                dp[i] %= 998244353
            if i - R[j] - 1 >= 0:
                dp[i] -= dpsum[i - R[j] - 1]
                dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= 998244353
    print(dp[N - 1])

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(1, N):
        for j in range(K):
            dp[i] += dpsum[max(i - L[j], 0)] - dpsum[max(i - R[j] - 1, 0)]
            dp[i] %= MOD
        dpsum[i + 1] = dpsum[i] + dp[i]
        dpsum[i + 1] %= MOD
    print(dp[N - 1])
solve()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    seg = []
    for _ in range(K):
        L, R = map(int, input().split())
        seg.append((L, R))
    dp = [0] * (N + 1)
    dp[1] = 1
    sdp = [0] * (N + 1)
    sdp[1] = 1
    for i in range(2, N + 1):
        for L, R in seg:
            if i - L < 0:
                continue
            dp[i] += sdp[i - L] - sdp[max(0, i - R - 1)]
        dp[i] %= 998244353
        sdp[i] = (sdp[i - 1] + dp[i]) % 998244353
    print(dp[N])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    LRs = []
    for _ in range(K):
        LR = list(map(int, input().split()))
        LRs.append(LR)
    #print(N, K)
    #print(LRs)

    #dp[i]: i番目のセルにたどり着く方法の総数
    dp = [0] * N
    dp[0] = 1

    #dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-L] (i-L >= 0)
    for i in range(1, N):
        for LR in LRs:
            L = LR[0]
            R = LR[1]
            if i - L >= 0:
                dp[i] += dp[i-L]
                dp[i] %= 998244353
            if i - R - 1 >= 0:
                dp[i] -= dp[i-R-1]
                dp[i] %= 998244353

    #print(dp)
    ans = dp[N-1]
    print(ans)

=======
Suggestion 8

def get_input():
    n, k = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(k)]
    return n, k, lrs

=======
Suggestion 9

def main():
    # Get input here
    N, K = map(int, input().strip().split())
    segments = []
    for i in range(K):
        segments.append(list(map(int, input().strip().split())))

    # Solve problems
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(1, N):
        for segment in segments:
            left = i - segment[1]
            right = i - segment[0]
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            dp[i] += dpsum[right] - dpsum[left]
        dp[i] %= 998244353
        dpsum[i+1] = dpsum[i] + dp[i]

    # Print output here
    print(dp[N-1])

=======
Suggestion 10

def main():
    pass
