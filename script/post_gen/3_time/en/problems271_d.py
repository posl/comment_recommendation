Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j-a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            if j-b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = []
    for i in range(n, 0, -1):
        if s-a[i-1] >= 0 and dp[i-1][s-a[i-1]]:
            ans.append("H")
            s -= a[i-1]
        else:
            ans.append("T")
            s -= b[i-1]
    print("".join(ans[::-1]))

=======
Suggestion 2

def solve():
    n, s = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + ab[i][0] <= s:
                    dp[i + 1][j + ab[i][0]] = True
                if j + ab[i][1] <= s:
                    dp[i + 1][j + ab[i][1]] = True

    if not dp[n][s]:
        print('No')
        return

    ans = []
    for i in reversed(range(n)):
        if s - ab[i][0] >= 0 and dp[i][s - ab[i][0]]:
            ans.append('T')
            s -= ab[i][0]
        else:
            ans.append('H')
            s -= ab[i][1]
    print('Yes')
    print(''.join(ans[::-1]))

=======
Suggestion 3

def main():
    N, S = [int(x) for x in input().split()]
    cards = []
    for i in range(N):
        cards.append([int(x) for x in input().split()])

    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            print("Yes")
            for j in range(N):
                if (i >> j) & 1:
                    print("H",end="")
                else:
                    print("T",end="")
            print()
            return
    print("No")

=======
Suggestion 4

def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1 == 1:
                    print("H", end="")
                else:
                    print("T", end="")
            print("")
            return
    print("No")
    return

=======
Suggestion 5

def get_input():
    n, s = map(int, input().split())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, input().split())))
    return n, s, cards

=======
Suggestion 6

def main():
    n, s = map(int, input().split())
    cards = []
    for i in range(n):
        cards.append(list(map(int, input().split())))
    #print(cards)
    for i in range(2**n):
        #print(i)
        bi = bin(i)[2:].zfill(n)
        #print(bi)
        total = 0
        for j in range(n):
            if bi[j] == '0':
                total += cards[j][0]
            else:
                total += cards[j][1]
        #print(total)
        if total == s:
            print('Yes')
            for j in range(n):
                if bi[j] == '0':
                    print('T', end='')
                else:
                    print('H', end='')
            print()
            return
    print('No')

=======
Suggestion 7

def main():
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, 1 << N):
        sum = 0
        ans = []
        for j in range(N):
            if i & (1 << j):
                sum += AB[j][0]
                ans.append('T')
            else:
                sum += AB[j][1]
                ans.append('H')
        if sum == S:
            print('Yes')
            print(''.join(ans))
            return
    print('No')

=======
Suggestion 8

def solve():
    N,S = map(int,input().split())
    cards = [list(map(int,input().split())) for i in range(N)]
    for i in range(1 << N):
        sum = 0
        for j in range(N):
            if (i >> j) & 1:
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == S:
            ans = ''
            for j in range(N):
                if (i >> j) & 1:
                    ans += 'H'
                else:
                    ans += 'T'
            return 'Yes\n' + ans
    return 'No'

=======
Suggestion 9

def f(n, s, cards):
    if n == 0:
        return s == 0
    if f(n - 1, s - cards[n - 1][0], cards):
        print('H', end='')
        return True
    if f(n - 1, s - cards[n - 1][1], cards):
        print('T', end='')
        return True
    return False

n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]

=======
Suggestion 10

def find_sum(n, s, cards):
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if (i & (1 << j)):
                sum += cards[j][0]
            else:
                sum += cards[j][1]

        if (sum == s):
            return i

    return -1
