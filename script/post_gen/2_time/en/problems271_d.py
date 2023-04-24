Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for _  in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+a[i] <= s:
                    dp[i+1][j+a[i]] = True
                if j+b[i] <= s:
                    dp[i+1][j+b[i]] = True
    if dp[n][s] == False:
        print("No")
        return
    print("Yes")
    ans = ""
    i = n
    j = s
    while i > 0:
        if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
            ans += "H"
            j -= a[i-1]
        else:
            ans += "T"
            j -= b[i-1]
        i -= 1
    print(ans[::-1])

main()

=======
Suggestion 2

def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        a, b = map(int, input().split())
        cards.append([a, b])
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i>>j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if (i>>j) & 1:
                    print("T", end="")
                else:
                    print("H", end="")
            print("")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + cards[i][0] <= s:
                    dp[i + 1][j + cards[i][0]] = True
                if j + cards[i][1] <= s:
                    dp[i + 1][j + cards[i][1]] = True
    if not dp[n][s]:
        print('No')
    else:
        print('Yes')
        ans = ''
        for i in range(n - 1, 0, -1):
            if dp[i][s] and dp[i - 1][s]:
                ans += 'T'
            elif dp[i][s - cards[i][0]] and dp[i - 1][s - cards[i][0]]:
                ans += 'H'
                s -= cards[i][0]
            else:
                ans += 'H'
                s -= cards[i][1]
        if s == cards[0][0]:
            ans += 'H'
        else:
            ans += 'T'
        print(ans[::-1])

=======
Suggestion 4

def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + cards[i][0] <= s:
                    dp[i + 1][j + cards[i][0]] = True
                if j + cards[i][1] <= s:
                    dp[i + 1][j + cards[i][1]] = True
    if not dp[n][s]:
        print('No')
        return
    print('Yes')
    ans = ''
    for i in range(n - 1, -1, -1):
        if s - cards[i][0] >= 0 and dp[i][s - cards[i][0]]:
            ans += 'H'
            s -= cards[i][0]
        else:
            ans += 'T'
            s -= cards[i][1]
    print(ans[::-1])

=======
Suggestion 5

def get_input():
    n, s = map(int, input().split())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    return n, s, ab

=======
Suggestion 6

def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(tuple(map(int, input().split())))
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a, b = cards[i]
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = 1
                if j+a <= S:
                    dp[i+1][j+a] = 1
                if j+b <= S:
                    dp[i+1][j+b] = 1
    if dp[N][S]:
        ans = ""
        for i in range(N-1, -1, -1):
            a, b = cards[i]
            if S-a >= 0 and dp[i][S-a]:
                ans += "T"
                S -= a
            else:
                ans += "H"
                S -= b
        print("Yes")
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 7

def solve(n, s, cards):
    for i in range(0, 2 ** n):
        sum = 0
        for j in range(0, n):
            if (i >> j) & 1 == 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            return True, i
    return False, 0

n, s = map(int, input().split())
cards = []
for i in range(0, n):
    cards.append(list(map(int, input().split())))

result, i = solve(n, s, cards)

=======
Suggestion 8

def solve(n,s,ab):
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == s:
            return i
    return -1

=======
Suggestion 9

def cardSum(n, S, cards):
    if n == 1:
        if cards[0][0] == S or cards[0][1] == S:
            return True, [0]
        else:
            return False, None
    else:
        for i in range(2**n):
            mask = i
            sum = 0
            indices = []
            for j in range(n):
                if mask % 2 == 0:
                    sum += cards[j][0]
                    indices.append(0)
                else:
                    sum += cards[j][1]
                    indices.append(1)
                mask //= 2
            if sum == S:
                return True, indices
        return False, None

=======
Suggestion 10

def check_sum(a, b, S):
    if S == a + b:
        return True
    else:
        return False
