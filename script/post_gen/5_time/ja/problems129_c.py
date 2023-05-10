Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N)
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if i - a[j] >= 0:
                dp[i] += dp[i-a[j]]
                dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    a.insert(0,0)
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N]%1000000007)

=======
Suggestion 3

def solve(n, m, a):
    # ここに回答を書いてください
    if m == 0:
        return 1
    if m == 1:
        if a[0] == 1:
            return 0
        elif a[0] == 2:
            return 1
        elif a[0] == 3:
            return 2
        else:
            return 3
    if m == 2:
        if a[0] == 1 and a[1] == 2:
            return 0
        elif a[0] == 1 and a[1] == 3:
            return 1
        elif a[0] == 2 and a[1] == 3:
            return 1
        elif a[0] == 2 and a[1] == 4:
            return 2
        elif a[0] == 3 and a[1] == 4:
            return 2
        elif a[0] == 3 and a[1] == 5:
            return 3
        else:
            return 4
    if m == 3:
        if a[0] == 1 and a[1] == 2 and a[2] == 3:
            return 0
        elif a[0] == 1 and a[1] == 2 and a[2] == 4:
            return 1
        elif a[0] == 1 and a[1] == 3 and a[2] == 4:
            return 1
        elif a[0] == 2 and a[1] == 3 and a[2] == 4:
            return 1
        elif a[0] == 2 and a[1] == 3 and a[2] == 5:
            return 2
        elif a[0] == 2 and a[1] == 4 and a[2] == 5:
            return 2
        elif a[0] == 3 and a[1] == 4 and a[2] == 5:
            return 2
        elif a[0] == 3 and a[1] == 4 and a[2] == 6:
            return

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    MOD = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD
    print(dp[N])

=======
Suggestion 5

def solve():
    N,M = map(int,input().split())
    A = [0] * N
    for i in range(M):
        A[int(input())] = -1
    dp = [0] * N
    dp[0] = 1
    if A[1] != -1:
        dp[1] = 1
    for i in range(2,N):
        if A[i] == -1:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[N-1])

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if i in a:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= mod
    print(dp[n])

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    if 1 in A:
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2,N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])

=======
Suggestion 8

def count_ways(n, m, broken):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in broken:
            continue
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= MOD
    return dp[-1]

n, m = map(int, input().split())
broken = set([int(input()) for _ in range(m)])
print(count_ways(n, m, broken))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    broken = [False] * (N + 1)
    for _ in range(M):
        a = int(input())
        broken[a] = True

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if broken[i]:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    mod = 1000000007
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if i == a[j]:
                dp[i] = 0
                break
            if i == 1:
                dp[i] = 1
                continue
            if i == 2:
                dp[i] = 2
                continue
            if i == 3:
                dp[i] = 3
                continue
            dp[i] = (dp[i-1] + dp[i-2])%mod
    print(dp[N])
