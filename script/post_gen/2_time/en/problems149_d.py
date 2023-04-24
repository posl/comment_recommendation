Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
        else:
            if T[i] == 'r' and T[i-K] != 'p':
                ans += P
                T = T[:i] + 'p' + T[i+1:]
            elif T[i] == 's' and T[i-K] != 'r':
                ans += R
                T = T[:i] + 'r' + T[i+1:]
            elif T[i] == 'p' and T[i-K] != 's':
                ans += S
                T = T[:i] + 's' + T[i+1:]
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
        else:
            if t[i] == 'r' and t[i-k] != 'r':
                ans += p
            elif t[i] == 's' and t[i-k] != 's':
                ans += r
            elif t[i] == 'p' and t[i-k] != 'p':
                ans += s
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    ans = 0
    for i in range(N):
        if i >= K:
            if T[i] == T[i-K]:
                T = T[:i] + 'x' + T[i+1:]
        if T[i] == 'r':
            ans += P
        elif T[i] == 's':
            ans += R
        elif T[i] == 'p':
            ans += S
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == T[i-K]:
                if i+K < N:
                    if T[i] == 'r' and T[i+K] == 'r':
                        T = T[:i]+'p'+T[i+1:]
                    elif T[i] == 's' and T[i+K] == 's':
                        T = T[:i]+'r'+T[i+1:]
                    elif T[i] == 'p' and T[i+K] == 'p':
                        T = T[:i]+'s'+T[i+1:]
                    else:
                        if T[i+K] == 'r':
                            T = T[:i]+'p'+T[i+1:]
                            score += P
                        elif T[i+K] == 's':
                            T = T[:i]+'r'+T[i+1:]
                            score += R
                        elif T[i+K] == 'p':
                            T = T[:i]+'s'+T[i+1:]
                            score += S
                else:
                    if T[i] == 'r':
                        T = T[:i]+'p'+T[i+1:]
                    elif T[i] == 's':
                        T = T[:i]+'r'+T[i+1:]
                    elif T[i] == 'p':
                        T = T[:i]+'s'+T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                elif T[i] == 'p':
                    score += S
    print(score)

=======
Suggestion 5

def RPS_Battle(N,K,R,S,P,T):
    score=0
    for i in range(N):
        if i<K:
            if T[i]=='r':
                score+=P
            elif T[i]=='s':
                score+=R
            elif T[i]=='p':
                score+=S
        else:
            if T[i]=='r' and T[i-K]!='r':
                score+=P
            elif T[i]=='s' and T[i-K]!='s':
                score+=R
            elif T[i]=='p' and T[i-K]!='p':
                score+=S
    return score

=======
Suggestion 6

def solve(n, k, r, s, p, t):
    dp = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(3):
            if t[i-1] == 'r':
                if j == 0:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + p
            elif t[i-1] == 's':
                if j == 1:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + r
            else:
                if j == 2:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + s
        if i >= k:
            for j in range(3):
                dp[i][j] = max(dp[i][j], dp[i-k][j])
    return max(dp[n])

=======
Suggestion 7

def get_max_score(n, k, r, s, p, t):
    max_score = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                max_score += p
            elif t[i] == 's':
                max_score += r
            elif t[i] == 'p':
                max_score += s
        else:
            if t[i] == 'r' and t[i-k] != 'p':
                max_score += p
                t[i-k] = 'p'
            elif t[i] == 's' and t[i-k] != 'r':
                max_score += r
                t[i-k] = 'r'
            elif t[i] == 'p' and t[i-k] != 's':
                max_score += s
                t[i-k] = 's'
    return max_score

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input().strip()
    win = {'r':P,'s':R,'p':S}
    ans = 0
    for i in range(N):
        if i < K:
            ans += win[T[i]]
        else:
            if T[i] == T[i-K]:
                if i+K < N and T[i] != T[i+K]:
                    ans += win[T[i]]
                    T = T[:i] + 'x' + T[i+1:]
            else:
                ans += win[T[i]]
    print(ans)

=======
Suggestion 9

def maxScore(N, K, R, S, P, T):
    # N: number of rounds
    # K: cannot use the hand used in the (i-K)-th round
    # R: Rock
    # S: Scissors
    # P: Paper
    # T: machine will play Rock, Paper, or Scissors in each round
    # return: maximum total score earned in the game
    score = 0
    prev = ""
    for i in range(N):
        if prev != T[i]:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
        else:
            if i >= K:
                if T[i-K] == "r":
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
                elif T[i-K] == "s":
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
                else:
                    if T[i] == "r":
                        score += P
                    elif T[i] == "s":
                        score += R
                    else:
                        score += S
        prev = T[i]
    return score
