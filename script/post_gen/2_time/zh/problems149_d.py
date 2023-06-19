Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # print(N, K, R, S, P, T)
    # print(T[:K])
    # print(T[K:])
    # print(T[K:] + T[:K])
    # print(T[K:] + T[:K] + T[K:] + T[:K])
    # print(T[K:] + T[:K] + T[K:] + T[:K] + T[K:] + T[:K])
    # print(T[K:] + T[:K] + T[K:]

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                if s < p:
                    score += p
                else:
                    score += s
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                if p < r:
                    score += r
                else:
                    score += p
            else:
                score += r
        elif t[i] == 'p':
            if i >= k and t[i-k] == 'p':
                if s < r:
                    score += r
                else:
                    score += s
            else:
                score += s
    print(score)

=======
Suggestion 3

def get_max_score(n, k, r, s, p, t):
    max_score = 0
    for i in range(n):
        if t[i] == 'r':
            max_score += p
        elif t[i] == 's':
            max_score += r
        else:
            max_score += s
    for i in range(n-k):
        if t[i] == 'r':
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
        elif t[i] == 's':
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
        else:
            if t[i+k] == 'r':
                max_score -= p
            elif t[i+k] == 's':
                max_score -= r
            else:
                max_score -= s
    return max_score

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
print(get_max_score(n, k, r, s, p, t))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    #print(n,k,r,s,p,t)
    #print(type(n),type(k),type(r),type(s),type(p),type(t))
    #print(len(t))
    #print(type(len(t)))
    #print(t[0])
    #print(type(t[0]))
    #print(t[0] == 'r')
    #print(type(t[0] == 'r'))
    #print(t[0] == 'r' and t[1] == 's')
    #print(type(t[0] == 'r' and t[1] == 's'))
    #print(t[0] == 'r' and t[1] == 's' and t[2] == 'r')
    #print(type(t[0] == 'r' and t[1] == 's' and t[2] == 'r'))
    #print(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p')
    #print(type(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p'))
    #print(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p' and t[4] == 's')
    #print(type(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p' and t[4] == 's'))
    #print(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p' and t[4] == 's' and t[5] == 's')
    #print(type(t[0] == 'r' and t[1] == 's' and t[2] == 'r' and t[3] == 'p' and t[4] == 's' and t[5] == 's'))
    #print(t[

=======
Suggestion 5

def problems149_d():
    pass

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #print(N,K,R,S,P,T)
    #dp[i][0]表示第i轮出石头时的最大分数
    #dp[i][1]表示第i轮出剪刀时的最大分数
    #dp[i][2]表示第i轮出布时的最大分数
    dp = [[0 for i in range(3)] for j in range(N)]
    for i in range(N):
        if T[i] == 'r':
            dp[i][0] = max(dp[i][0],dp[i-1][1]+S,dp[i-1][2]+P)
            dp[i][1] = max(dp[i][1],dp[i-1][0])
            dp[i][2] = max(dp[i][2],dp[i-1][0])
        elif T[i] == 's':
            dp[i][0] = max(dp[i][0],dp[i-1][1])
            dp[i][1] = max(dp[i][1],dp[i-1][2]+P,dp[i-1][0]+R)
            dp[i][2] = max(dp[i][2],dp[i-1][1])
        else:
            dp[i][0] = max(dp[i][0],dp[i-1][2]+P,dp[i-1][1]+S)
            dp[i][1] = max(dp[i][1],dp[i-1][0])
            dp[i][2] = max(dp[i][2],dp[i-1][0])
        if i >= K:
            dp[i][0] = max(dp[i][0],dp[i-K][0],dp[i-K][1],dp[i-K][2])
            dp[i][1] = max(dp[i][1],dp[i-K][0],dp[i-K][1],dp[i-K][2])
            dp[i][2] = max(dp[i][2],dp[i-K][0],dp[i-K][1],dp[i-K][2])
    #print(dp)
    print(max(dp[N-1][0],dp[N-1][1],dp[N-1][2]))

solve()

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    for i in range(1,n+1):
        if t[i-1] == 'r':
            dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + p
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        elif t[i-1] == 's':
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + r
            dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        else:
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + s
        if i >= k:
            for j in range(3):
                dp[i][j] = max(dp[i][j],dp[i-k][j])
    ans = 0
    for i in range(n+1):
        for j in range(3):
            ans = max(ans,dp[i][j])
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # dp[i][j] = i回目までにjを選んだときの最大得点
    dp = [[0 for i in range(3)] for j in range(N+1)]
    for i in range(N):
        # 今回の手
        t = T[i]
        # 前回の手
        if i-K >= 0:
            prev = T[i-K]
        else:
            prev = "x"

        if t == "r":
            dp[i+1][0] = max(dp[i+1][0], dp[i][1] + P, dp[i][2] + P)
            if prev != "r":
                dp[i+1][0] = max(dp[i+1][0], dp[i][0] + R)
        elif t == "s":
            dp[i+1][1] = max(dp[i+1][1], dp[i][0] + R, dp[i][2] + R)
            if prev != "s":
                dp[i+1][1] = max(dp[i+1][1], dp[i][1] + S)
        elif t == "p":
            dp[i+1][2] = max(dp[i+1][2], dp[i][0] + S, dp[i][1] + S)
            if prev != "p":
                dp[i+1][2] = max(dp[i+1][2], dp[i][2] + P)

    print(max(dp[N]))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i < k:
                ans += p
            elif t[i - k] == 'r':
                ans += 0
            else:
                ans += p
        elif t[i] == 's':
            if i < k:
                ans += r
            elif t[i - k] == 's':
                ans += 0
            else:
                ans += r
        elif t[i] == 'p':
            if i < k:
                ans += s
            elif t[i - k] == 'p':
                ans += 0
            else:
                ans += s
    print(ans)

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if T[i] == 'r':
            if i < K or T[i - K] != 'r':
                ans += P
        elif T[i] == 's':
            if i < K or T[i - K] != 's':
                ans += R
        elif T[i] == 'p':
            if i < K or T[i - K] != 'p':
                ans += S
    print(ans)

solve()
