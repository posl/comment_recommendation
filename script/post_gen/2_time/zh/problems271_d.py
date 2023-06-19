Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n,s = map(int,input().split())
    cards = []
    for i in range(n):
        card = list(map(int,input().split()))
        cards.append(card)
    return n,s,cards

=======
Suggestion 2

def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    # print(N, S, cards)
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= cards[i][0]:
                dp[i+1][j] |= dp[i][j-cards[i][0]]
            if j >= cards[i][1]:
                dp[i+1][j] |= dp[i][j-cards[i][1]]
    if dp[N][S]:
        print("Yes")
        ans = ""
        i, j = N, S
        while i > 0 and j > 0:
            if j >= cards[i-1][0] and dp[i-1][j-cards[i-1][0]]:
                ans += "H"
                j -= cards[i-1][0]
            else:
                ans += "T"
                j -= cards[i-1][1]
            i -= 1
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 3

def solve(n, s, a, b):
    dp = [[False for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j < a[i] and j < b[i]:
                dp[i+1][j] = False
            elif j < a[i]:
                dp[i+1][j] = dp[i][j-b[i]]
            elif j < b[i]:
                dp[i+1][j] = dp[i][j-a[i]]
            else:
                dp[i+1][j] = dp[i][j-a[i]] or dp[i][j-b[i]]
    if dp[n][s]:
        print("Yes")
        res = ""
        for i in range(n, 0, -1):
            if s >= a[i-1] and dp[i-1][s-a[i-1]]:
                res = "H" + res
                s -= a[i-1]
            else:
                res = "T" + res
                s -= b[i-1]
        print(res)
    else:
        print("No")

=======
Suggestion 4

def solve(n, s, cards):
    for i in range(2 ** n):
        visible = [0] * n
        for j in range(n):
            if i >> j & 1:
                visible[j] = 1

        sum = 0
        for j in range(n):
            if visible[j]:
                sum += cards[j][0]
            else:
                sum += cards[j][1]

        if sum == s:
            print("Yes")
            for j in range(n):
                if visible[j]:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return

    print("No")

=======
Suggestion 5

def dfs(i, sum):
    if i == n:
        return sum == S
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False

=======
Suggestion 6

def solve(n, s, cards):
    if n == 1:
        if s == cards[0][0] or s == cards[0][1]:
            return True, [0]
        else:
            return False, []
    else:
        for i in range(2 ** n):
            bin_i = bin(i)[2:].zfill(n)
            sum = 0
            for j in range(n):
                if bin_i[j] == '0':
                    sum += cards[j][0]
                else:
                    sum += cards[j][1]
            if sum == s:
                return True, bin_i
        return False, []

n, s = map(int, input().split())
cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))
res, bin_i = solve(n, s, cards)

=======
Suggestion 7

def check_sum(n, s, cards):
    if n < 1:
        return False
    if s < 1:
        return False
    if len(cards) != n:
        return False

    # 筛选出所有的可能性
    # 1. 每张牌都正面朝上
    # 2. 每张牌都背面朝上
    # 3. 每张牌都正面朝上或者背面朝上

    # 1. 每张牌都正面朝上
    sum = 0
    for i in range(n):
        sum += cards[i][0]
    if sum == s:
        return True

    # 2. 每张牌都背面朝上
    sum = 0
    for i in range(n):
        sum += cards[i][1]
    if sum == s:
        return True

    # 3. 每张牌都正面朝上或者背面朝上
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                if k == i:
                    sum += cards[k][0]
                elif k == j:
                    sum += cards[k][1]
                else:
                    if cards[k][0] > cards[k][1]:
                        sum += cards[k][0]
                    else:
                        sum += cards[k][1]
            if sum == s:
                return True

    return False

=======
Suggestion 8

def solve():
    N, S = map(int, input().split())
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append((a, b))
    dp = [[False for i in range(S + 1)] for j in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i][0]:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i][0]]
            if j >= A[i][1]:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i][1]]
    if not dp[N][S]:
        print("No")
        return
    print("Yes")
    ans = ""
    for i in range(N - 1, -1, -1):
        if S >= A[i][0] and dp[i][S - A[i][0]]:
            ans += "H"
            S -= A[i][0]
        else:
            ans += "T"
            S -= A[i][1]
    print(ans[::-1])

=======
Suggestion 9

def main():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] = True if j is reachable using cards[0:i]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        a, b = cards[i]
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a <= S:
                    dp[i + 1][j + a] = True
                if j + b <= S:
                    dp[i + 1][j + b] = True

    if dp[N][S]:
        print("Yes")
        ans = ["H"] * N
        for i in range(N - 1, 0, -1):
            a, b = cards[i]
            if S - a >= 0 and dp[i][S - a]:
                ans[i] = "T"
                S -= a
            else:
                ans[i] = "H"
                S -= b
        ans[0] = "H" if S - cards[0][0] >= 0 else "T"
        print("".join(ans))
    else:
        print("No")

=======
Suggestion 10

def solve(card, S):
    # 将第i张牌的正面可见，第j张牌的背面可见，第k张牌的背面可见
    dp = [[[False for _ in range(S+1)] for _ in range(S+1)] for _ in range(len(card)+1)]
    dp[0][0][0] = True
    for i in range(len(card)):
        for j in range(S+1):
            for k in range(S+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+card[i][0] <= S:
                        dp[i+1][j+card[i][0]][k] = True
                    if k+card[i][1] <= S:
                        dp[i+1][j][k+card[i][1]] = True
    if not dp[len(card)][S][S]:
        return False, []
    else:
        ans = []
        i = len(card)
        j = S
        k = S
        while i > 0:
            if dp[i-1][j][k]:
                ans.append('H')
            elif j-card[i-1][0] >= 0 and dp[i-1][j-card[i-1][0]][k]:
                ans.append('T')
                j -= card[i-1][0]
            else:
                ans.append('F')
                k -= card[i-1][1]
            i -= 1
        return True, ans[::-1]
