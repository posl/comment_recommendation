Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     LR   =   [ tuple ( map ( int ,   input (). split ()))   for   _   in   range ( K )] 
     MOD   =   998244353 

     dp   =   [ 0 ]   *   ( N + 1 ) 
     dp [ 0 ]   =   1 
     for   i   in   range ( N ): 
         for   l ,   r   in   LR : 
             dp [ min ( i + r ,   N )]   +=   dp [ max ( i + l ,   0 )] 
             dp [ min ( i + r ,   N )]   %=   MOD 

     print ( dp [ - 1 ])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for l, r in LR:
            if i + l < N:
                dp[i + l] += dp[i]
                dp[i + l] %= MOD
            if i + r + 1 < N:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= MOD
    for i in range(1, N):
        dp[i] += dp[i - 1]
        dp[i] %= MOD
    print(dp[N - 1])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(k)]
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for l, r in lrs:
            dp[i] += dp[i - l] - dp[i - r - 1]
    print((dp[n] % 998244353 + 998244353) % 998244353)

=======
Suggestion 4

def solve(n, k, lrs):
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        for l, r in lrs:
            dp[i + l] += dp[i]
            dp[i + l] %= mod
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= mod
    return dp[n]

n, k = map(int, input().split())
lrs = [map(int, input().split()) for _ in range(k)]
print(solve(n, k, lrs))

=======
Suggestion 5

def solve(N, K, LR):
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
    return dp[N]

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    l = []
    r = []
    for i in range(k):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = dp[1] + 1
    s = [0]*(n+1)
    s[1] = 1
    s[2] = 2
    for i in range(3,n+1):
        for j in range(k):
            dp[i] += s[i-l[j]] - s[i-r[j]-1]
        dp[i] %= 998244353
        s[i] = s[i-1] + dp[i]
    print(dp[n])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(K):
        S.append(list(map(int, input().split())))

    MOD = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(1, N):
        for j in range(K):
            l, r = S[j]
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
    print(dp[N])

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        for lr in lrs:
            l, r = lr
            if i + l < n:
                dp[i + l] += dp[i]
                dp[i + l] %= mod
            if i + r + 1 < n:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= mod
    for i in range(n - 1):
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
    print(dp[n - 1])

=======
Suggestion 9

def  main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    dp = [0] * N
    dp[0] = 1
    sumdp = [0] * (N + 1)
    sumdp[1] = 1
    for i in range(N):
        for l, r in LR:
            dp[i] += sumdp[max(0, i - l + 1)] - sumdp[max(0, i - r)]
        dp[i] %= 998244353
        sumdp[i + 1] = sumdp[i] + dp[i]
    print(dp[-1])

=======
Suggestion 10

def main():
  import sys
  readline = sys.stdin.readline
  N, K = map(int, readline().split())
  LR = [list(map(int, readline().split())) for _ in range(K)]
  LR.sort()
  MOD = 998244353
  dp = [0] * (N + 1)
  dp[1] = 1
  for i in range(N):
    for l, r in LR:
      if i + l > N:
        break
      dp[i + l] += dp[i]
      dp[i + l] %= MOD
      if i + r + 1 <= N:
        dp[i + r + 1] -= dp[i]
        dp[i + r + 1] %= MOD
  for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    dp[i] %= MOD
  print(dp[N])
