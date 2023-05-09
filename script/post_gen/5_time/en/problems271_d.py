Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))

    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ""
            for j in range(N):
                if (i >> j) & 1:
                    ans += "H"
                else:
                    ans += "T"
            print("Yes")
            print(ans)
            return
    print("No")

=======
Suggestion 2

def get_input():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))
    return N, S, cards

=======
Suggestion 3

def main():
    n, s = map(int, input().split())
    cards = []
    for _ in range(n):
        a, b = map(int, input().split())
        cards.append([a, b])
    cards.sort(reverse=True)
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                if j + cards[i][0] <= s:
                    dp[i+1][j+cards[i][0]] = True
                if j + cards[i][1] <= s:
                    dp[i+1][j+cards[i][1]] = True
    if dp[n][s]:
        print("Yes")
        ans = ""
        for i in range(n-1, -1, -1):
            if s - cards[i][0] >= 0 and dp[i][s-cards[i][0]]:
                ans += "H"
                s -= cards[i][0]
            else:
                ans += "T"
                s -= cards[i][1]
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 4

def solve():
    N, S = map(int, input().split())
    ab = []
    for _ in range(N):
        a, b = map(int, input().split())
        ab.append((a, b))
    dp = [[0 for _ in range(S + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 0:
                continue
            if j + ab[i][0] <= S:
                dp[i + 1][j + ab[i][0]] = 1
            if j + ab[i][1] <= S:
                dp[i + 1][j + ab[i][1]] = 1
    if dp[N][S] == 0:
        print('No')
        return
    print('Yes')
    ans = ''
    for i in range(N - 1, -1, -1):
        if S - ab[i][0] >= 0 and dp[i][S - ab[i][0]] == 1:
            ans += 'T'
            S -= ab[i][0]
        else:
            ans += 'H'
            S -= ab[i][1]
    print(ans[::-1])

=======
Suggestion 5

def solve(n, s, a):
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j][0]
            else:
                sum += a[j][1]
        if sum == s:
            return True, i
    return False, 0

n, s = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
result, ans = solve(n, s, a)

=======
Suggestion 6

def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    print(cards)
    for i in range(2**n):
        ans = []
        for j in range(n):
            if i & (1 << j):
                ans.append(cards[j][0])
            else:
                ans.append(cards[j][1])
        print(ans)
        if sum(ans) == s:
            print("Yes")
            print(ans)
            return
    print("No")

=======
Suggestion 7

def solve(N, S, cards):
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if ((i >> j) & 1) == 0:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ""
            for j in range(N):
                if ((i >> j) & 1) == 0:
                    ans += "H"
                else:
                    ans += "T"
            return "Yes\n" + ans
    return "No"

=======
Suggestion 8

def main():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    for i in range(2**N):
        tmp = S
        tmp_cards = []
        for j in range(N):
            if (i >> j) & 1:
                tmp -= cards[j][0]
                tmp_cards.append('H')
            else:
                tmp -= cards[j][1]
                tmp_cards.append('T')
        if tmp == 0:
            print('Yes')
            print(''.join(tmp_cards))
            exit()
    print('No')

=======
Suggestion 9

def solve():
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] = (i番目までのカードを使って、表をjにすることができるか)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + AB[i][0] <= S:
                    dp[i + 1][j + AB[i][0]] = True
                if j + AB[i][1] <= S:
                    dp[i + 1][j + AB[i][1]] = True

    if dp[N][S]:
        ans = []
        for i in range(N - 1, 0, -1):
            if S - AB[i][0] >= 0 and dp[i][S - AB[i][0]]:
                ans.append('H')
                S -= AB[i][0]
            else:
                ans.append('T')
                S -= AB[i][1]
        ans.reverse()
        ans.append('H' if S == AB[0][0] else 'T')
        print(''.join(ans))
    else:
        print('No')

=======
Suggestion 10

def findSum(S, N, A, B):
    for i in range(N):
        if A[i] >= S:
            return i, 'F'
        if B[i] >= S:
            return i, 'B'
    return -1, 'F'
