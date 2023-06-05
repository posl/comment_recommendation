Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    return N, S, cards

=======
Suggestion 2

def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append((a, b))
    # print(cards)
    # print(n, s)
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    # print(cards[4][1])
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    # print(cards[4][1])
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    # print(cards[4][1])
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    # print(cards[4][1])
    # print(cards[0][0])
    # print(cards[0][1])
    # print(cards[1][0])
    # print(cards[1][1])
    # print(cards[2][0])
    # print(cards[2][1])
    # print(cards[3][0])
    # print(cards[3][1])
    # print(cards[4][0])
    #

=======
Suggestion 3

def main():
    n,s = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a,b)

    #dp[i][j]表示前i张牌中，和为j的情况下，第i张牌的正反面状态
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = 2
                if j+b[i] <= s:
                    dp[i+1][j+b[i]] = 3
    #print(dp)
    if dp[n][s] == 0:
        print("No")
    else:
        print("Yes")
        ans = ""
        for i in range(n,0,-1):
            if dp[i][s] == 2:
                ans += "H"
                s -= a[i-1]
            else:
                ans += "T"
                s -= b[i-1]
        print(ans[::-1])

=======
Suggestion 4

def solve():
    N, S = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + A[i][0] <= S:
                    dp[i + 1][j + A[i][0]] = True
                if j + A[i][1] <= S:
                    dp[i + 1][j + A[i][1]] = True

    if dp[N][S]:
        print("Yes")
        ans = ["T"] * N
        i = N - 1
        j = S
        while i >= 0:
            if j - A[i][0] >= 0 and dp[i][j - A[i][0]]:
                ans[i] = "H"
                j -= A[i][0]
            elif j - A[i][1] >= 0 and dp[i][j - A[i][1]]:
                ans[i] = "T"
                j -= A[i][1]
            else:
                assert False
            i -= 1
        print("".join(ans))
    else:
        print("No")


solve()

=======
Suggestion 5

def solve(n, s, cards):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return True, i
    return False, 0

=======
Suggestion 6

def test():
    N = 3
    S = 11
    a = [1, 2, 5]
    b = [4, 3, 7]
    # print(N, S, a, b)
    ans = solve(N, S, a, b)
    print(ans)

=======
Suggestion 7

def main():
    N, S = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    ans = []
    for i in range(N):
        if AB[i][0] == S:
            ans.append("H")
        elif AB[i][1] == S:
            ans.append("T")
        elif AB[i][0] + AB[i][1] == S:
            ans.append("HT")
        else:
            ans.append("N")
    if "N" in ans:
        print("No")
    else:
        print("Yes")
        print("".join(ans))

=======
Suggestion 8

def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                if j + a[i] <= s:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= s:
                    dp[i+1][j+b[i]] = True

    if dp[n][s]:
        print("Yes")
        ans = ""
        i = n
        j = s
        while i > 0:
            if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans = "H" + ans
                j -= a[i-1]
            else:
                ans = "T" + ans
                j -= b[i-1]
            i -= 1
        print(ans)
    else:
        print("No")

=======
Suggestion 9

def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j + a[i] <= s:
                    dp[i+1][j+a[i]] = 1
                if j + b[i] <= s:
                    dp[i+1][j+b[i]] = 1
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = ""
    for i in range(n-1, -1, -1):
        if s - a[i] >= 0 and dp[i][s-a[i]]:
            ans += "H"
            s -= a[i]
        else:
            ans += "T"
            s -= b[i]
    print(ans[::-1])

=======
Suggestion 10

def f(n, s, a, b):
    if n == 0:
        return s == 0
    if f(n-1, s-a[n-1], a, b):
        print('T', end='')
        return True
    if f(n-1, s-b[n-1], a, b):
        print('H', end='')
        return True
    return False
