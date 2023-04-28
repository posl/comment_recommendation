Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K or T[i] != T[i-K]:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            else:
                ans += S
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i >= K and T[i] == T[i-K]:
            T = T[:i] + 'x' + T[i+1:]
        else:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            elif T[i] == 'p':
                ans += S
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    score = 0
    for i in range(N):
        if T[i] == "r":
            if i >= K:
                if T[i-K] == "r":
                    T[i] = "x"
                else:
                    score += P
            else:
                score += P
        elif T[i] == "s":
            if i >= K:
                if T[i-K] == "s":
                    T[i] = "x"
                else:
                    score += R
            else:
                score += R
        else:
            if i >= K:
                if T[i-K] == "p":
                    T[i] = "x"
                else:
                    score += S
            else:
                score += S
    print(score)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    score = 0
    for i in range(N):
        if T[i] == "r":
            if i - K >= 0:
                if T[i - K] == "r":
                    T[i] = "x"
                else:
                    score += P
            else:
                score += P
        elif T[i] == "s":
            if i - K >= 0:
                if T[i - K] == "s":
                    T[i] = "x"
                else:
                    score += R
            else:
                score += R
        elif T[i] == "p":
            if i - K >= 0:
                if T[i - K] == "p":
                    T[i] = "x"
                else:
                    score += S
            else:
                score += S
    print(score)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    t = list(t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k:
                if t[i - k] == 'r':
                    t[i] = 'x'
                else:
                    score += r
            else:
                score += r
        elif t[i] == 's':
            if i >= k:
                if t[i - k] == 's':
                    t[i] = 'x'
                else:
                    score += s
            else:
                score += s
        elif t[i] == 'p':
            if i >= k:
                if t[i - k] == 'p':
                    t[i] = 'x'
                else:
                    score += p
            else:
                score += p
    print(score)

=======
Suggestion 6

def main():
    # Get input here
    N, K = map(int, input().strip().split())
    R, S, P = map(int, input().strip().split())
    T = input().strip()
    # Calculate result here
    result = get_max_score(N, K, R, S, P, T)
    # Print output here
    print(result)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    r,s,p = map(int, input().split())
    t = input()
    point = 0
    for i in range(n):
        if t[i] == "r" and i < k:
            point += p
        elif t[i] == "r" and i >= k and t[i-k] != "r":
            point += p
        elif t[i] == "s" and i < k:
            point += r
        elif t[i] == "s" and i >= k and t[i-k] != "s":
            point += r
        elif t[i] == "p" and i < k:
            point += s
        elif t[i] == "p" and i >= k and t[i-k] != "p":
            point += s
    print(point)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(k):
        t2 = t[i::k]
        t3 = t2.replace('r', 'p').replace('s', 'r').replace('p', 's')
        t4 = t3.replace('p', 'r')
        ans += t4.count('r') * r + t4.count('s') * s + t4.count('p') * p
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    def get_score(hand):
        if hand == "r":
            return P
        elif hand == "s":
            return R
        elif hand == "p":
            return S

    def get_hand(opp_hand):
        if opp_hand == "r":
            return "p"
        elif opp_hand == "s":
            return "r"
        elif opp_hand == "p":
            return "s"

    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = get_score(get_hand(T[0]))
    dp[0][1] = get_score(get_hand(T[0]))
    dp[0][2] = get_score(get_hand(T[0]))

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + get_score(get_hand(T[i]))
        dp[i][1] = dp[i-1][1] + get_score(get_hand(T[i]))
        dp[i][2] = dp[i-1][2] + get_score(get_hand(T[i]))
        if i >= K:
            dp[i][0] = max(dp[i][0], dp[i-K][1] + get_score(get_hand(T[i])))
            dp[i][1] = max(dp[i][1], dp[i-K][2] + get_score(get_hand(T[i])))
            dp[i][2] = max(dp[i][2], dp[i-K][0] + get_score(get_hand(T[i])))

    print(max(dp[N-1]))


main()

=======
Suggestion 10

def rpsbattle(n, k, r, s, p, t):
    # print(n, k, r, s, p, t)
    # print(r, s, p)
    # print(t)
    # print(t[0])
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                score += 0
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                score += 0
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                score += 0
            else:
                score += s
    return score
