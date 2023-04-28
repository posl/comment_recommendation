Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, s = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    # dp[i][j] = 1 if it is possible to make sum j using the first i cards
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                if j + a[i] <= s:
                    dp[i + 1][j + a[i]] = 1
                if j + b[i] <= s:
                    dp[i + 1][j + b[i]] = 1

    if dp[n][s] == 0:
        print("No")
        return

    print("Yes")
    ans = ["H"] * n
    i = n
    j = s
    while i > 0 and j > 0:
        if j >= a[i - 1] and dp[i - 1][j - a[i - 1]]:
            ans[i - 1] = "H"
            j -= a[i - 1]
        else:
            ans[i - 1] = "T"
            j -= b[i - 1]
        i -= 1
    print("".join(ans))

=======
Suggestion 2

def solve():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for j in range(s+1)] for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = True
                if j+b[i] <= s:
                    dp[i+1][j+b[i]] = True
    if not dp[n][s]:
        print('No')
        return
    print('Yes')
    ans = ['0' for i in range(n)]
    for i in range(n-1, -1, -1):
        if s-a[i] >= 0 and dp[i][s-a[i]]:
            ans[i] = 'A'
            s -= a[i]
        else:
            ans[i] = 'B'
            s -= b[i]
    print(''.join(ans))

=======
Suggestion 3

def main():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))

    dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + cards[i][0] <= S:
                    dp[i + 1][j + cards[i][0]] = True
                if j + cards[i][1] <= S:
                    dp[i + 1][j + cards[i][1]] = True

    if not dp[N][S]:
        print('No')
    else:
        print('Yes')
        ans = ''
        for i in reversed(range(N)):
            if S - cards[i][0] >= 0 and dp[i][S - cards[i][0]]:
                ans += 'T'
                S -= cards[i][0]
            else:
                ans += 'H'
                S -= cards[i][1]
        print(ans[::-1])

=======
Suggestion 4

def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print('Yes')
            for j in range(n):
                if (i >> j) & 1:
                    print('H', end='')
                else:
                    print('T', end='')
            print()
            return
    print('No')

=======
Suggestion 5

def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        a, b = map(int, input().split())
        cards.append([a, b])
    print(cards)
    print(N, S)

=======
Suggestion 6

def solve(n, s, a, b):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += a[j]
            else:
                sum += b[j]
        if sum == s:
            return i
    return -1

=======
Suggestion 7

def solve(n, s, cards):
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if ((i >> j) & 1) == 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]

        if sum == s:
            return i

    return -1

n, s = map(int, input().split())
cards = []
for i in range(n):
    cards.append(list(map(int, input().split())))

ans = solve(n, s, cards)

=======
Suggestion 8

def solve(n,s,ab):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == s:
            return i
    return -1

n,s = map(int,input().split())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

ret = solve(n,s,ab)

=======
Suggestion 9

def solve(n, s, cards):
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return i
    return -1

n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]
result = solve(n, s, cards)

=======
Suggestion 10

def solve(n,s,card):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if ((i >> j) & 1):
                sum += card[j][0]
            else:
                sum += card[j][1]
        if sum == s:
            return i
    return -1

n,s = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(n)]
ans = solve(n,s,card)
