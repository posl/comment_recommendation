Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i - k >= 0 and t[i - k] == 'r':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += p
        elif t[i] == 's':
            if i - k >= 0 and t[i - k] == 's':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += r
        elif t[i] == 'p':
            if i - k >= 0 and t[i - k] == 'p':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += s
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += s
    print(score)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if T[i] == 'r':
            if i >= K and T[i-K] == 'r':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += P
        elif T[i] == 's':
            if i >= K and T[i-K] == 's':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += R
        else:
            if i >= K and T[i-K] == 'p':
                T = T[:i] + 'x' + T[i+1:]
            else:
                score += S
    print(score)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i - k] == 'r':
                t[i] = 'x'
            else:
                ans += p
        elif t[i] == 's':
            if i >= k and t[i - k] == 's':
                t[i] = 'x'
            else:
                ans += r
        else:
            if i >= k and t[i - k] == 'p':
                t[i] = 'x'
            else:
                ans += s
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    for i in range(N):
        if T[i] == 'r':
            T[i] = 'p'
        elif T[i] == 's':
            T[i] = 'r'
        else:
            T[i] = 's'
    T = "".join(T)
    T = T.replace('r','R')
    T = T.replace('s','S')
    T = T.replace('p','P')
    #print(T)
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'R':
                ans += R
            elif T[i] == 'S':
                ans += S
            else:
                ans += P
        else:
            if T[i] == 'R':
                if T[i-K] == 'R':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += R
            elif T[i] == 'S':
                if T[i-K] == 'S':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += S
            else:
                if T[i-K] == 'P':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += P
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    t = list(t)

    score = 0
    for i in range(n):
        if i >= k and t[i] == t[i-k] and t[i-k] != "x":
            t[i] = "x"
        else:
            if t[i] == "r":
                score += p
            elif t[i] == "s":
                score += r
            elif t[i] == "p":
                score += s

    print(score)

=======
Suggestion 7

def rps():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i] + 's' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i] + 'p' + t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i] + 'r' + t[i+1:]
            else:
                score += s
    return score

print(rps())

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # 0:G, 1:C, 2:P
    hands = {'r': 0, 's': 1, 'p': 2}

    # 0:G, 1:C, 2:P
    scores = [P, R, S]

    # 0:G, 1:C, 2:P
    dp = [[0 for _ in range(3)] for _ in range(N+1)]

    for i in range(N):
        for j in range(3):
            if i < K or dp[i-K][(j+1)%3] < dp[i-K][(j+2)%3]:
                dp[i+1][j] = dp[i][j] + scores[j] * (1 if hands[T[i]] == j else 0)
            else:
                dp[i+1][j] = dp[i-K][j] + scores[j] * (1 if hands[T[i]] == j else 0)

    print(max(dp[N]))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    # dp[i][j]: i回目の手でjを出した時の最大得点
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    # 1回目の手は何でも良い
    for i in range(3):
        dp[1][i] = [r, s, p][i]

    for i in range(2, n+1):
        # i回目の手でjを出すときの最大得点
        for j in range(3):
            # i回目の手でjを出すときの得点
            point = [r, s, p][j]
            # i回目の手でjを出すときの得点を加える
            dp[i][j] = dp[i-1][j] + point

            # i回目の手でjを出すとき、i-k回目の手でjを出していたら、i回目の手でjを出せないので、i-k回目の手でjを出さない
            if t[i-1] == t[i-k-1]:
                # i-k回目の手でjを出していたときの最大得点
                max_point = max(dp[i-k-1])
                # i-k回目の手でjを出していたときの最大得点を引く
                dp[i][j] -= max_point

    print(max(dp[n]))

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # dp[i][j] = i回戦までの最大得点。j=0: r, j=1: s, j=2: p
    dp = [[0] * 3 for _ in range(N+1)]

    for i in range(N):
        if T[i] == 'r':
            dp[i+1][0] = max(dp[i][1], dp[i][2]) + P
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        elif T[i] == 's':
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2]) + R
            dp[i+1][2] = max(dp[i][0], dp[i][1])
        else:
            dp[i+1][0] = max(dp[i][1], dp[i][2])
            dp[i+1][1] = max(dp[i][0], dp[i][2])
            dp[i+1][2] = max(dp[i][0], dp[i][1]) + S

        if i >= K:
            if T[i-K] == 'r':
                dp[i+1][0] = max(dp[i+1][0], dp[i-K][0])
            elif T[i-K] == 's':
                dp[i+1][1] = max(dp[i+1][1], dp[i-K][1])
            else:
                dp[i+1][2] = max(dp[i+1][2], dp[i-K][2])

    print(max(dp[N]))
