Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,s = map(int,input().split())
    cards = [list(map(int,input().split())) for _ in range(n)]
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += cards[j][0]
            else:
                sum += cards[j][1]
        if sum == s:
            ans = []
            for j in range(n):
                if i & (1<<j):
                    ans.append('T')
                else:
                    ans.append('H')
            print('Yes')
            print(''.join(ans))
            return
    print('No')

=======
Suggestion 2

def card_sum():
    N, S = map(int, input().split())
    card_list = [list(map(int, input().split())) for _ in range(N)]
    for i in range(2**N):
        card_sum = 0
        card_H_T = []
        for j in range(N):
            if ((i >> j) & 1):
                card_sum += card_list[j][0]
                card_H_T.append("H")
            else:
                card_sum += card_list[j][1]
                card_H_T.append("T")
        if card_sum == S:
            print("Yes")
            print("".join(card_H_T))
            exit()
    print("No")

card_sum()

=======
Suggestion 3

def dfs(i, s):
    global N, S, A, B, res
    if i == N:
        if s == S:
            res = True
        return
    dfs(i+1, s+A[i])
    dfs(i+1, s+B[i])

N, S = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

res = False
dfs(0, 0)
print('Yes' if res else 'No')

=======
Suggestion 4

def dfs(i, sum):
    if i == n:
        if sum == s:
            return True
        else:
            return False
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum+a[i]):
        ans.append("T")
        return True
    if dfs(i+1, sum+b[i]):
        ans.append("H")
        return True
    return False

n, s = map(int, input().split())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = []

=======
Suggestion 5

def main():
    N,S = map(int,input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int,input().split())))
    #print(cards)
    for i in range(2**N):
        sum = 0
        temp = i
        card = []
        for j in range(N):
            card.append(temp%2)
            temp = temp//2
        #print(card)
        for k in range(N):
            if card[k] == 0:
                sum += cards[k][0]
            else:
                sum += cards[k][1]
        if sum == S:
            print("Yes")
            for k in range(N):
                if card[k] == 0:
                    print("T",end="")
                else:
                    print("H",end="")
            print("")
            break
    else:
        print("No")

=======
Suggestion 6

def main():
    n, s = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 'No'
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j][0]
            else:
                sum += a[j][1]
        if sum == s:
            ans = 'Yes'
            break
    print(ans)
    if ans == 'Yes':
        for j in range(n):
            if (i>>j)&1:
                print('T', end='')
            else:
                print('H', end='')
        print()

=======
Suggestion 7

def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, 2 ** n):
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
                    print('T', end='')
                else:
                    print('H', end='')
            print()
            return
    print('No')

=======
Suggestion 8

def check(N,S,card):
    for i in range(N):
        card[i][0] = int(card[i][0])
        card[i][1] = int(card[i][1])
    for i in range(N):
        for j in range(N):
            if card[i][0] + card[j][1] == S:
                return True
    return False

=======
Suggestion 9

def main():
    n, s = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1 << n):
        t = 0
        for j in range(n):
            if (i >> j) & 1:
                t += a[j][1]
            else:
                t += a[j][0]
        if t == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1:
                    print("T", end="")
                else:
                    print("H", end="")
            print()
            exit()
    print("No")

=======
Suggestion 10

def solve():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])

    dp = [[False for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j - a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            elif j - b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True

    if not dp[n][s]:
        print("No")
        return

    ans = [""] * n
    for i in range(n)[::-1]:
        if s - a[i] >= 0 and dp[i][s-a[i]]:
            s -= a[i]
            ans[i] = "H"
        else:
            s -= b[i]
            ans[i] = "T"

    print("Yes")
    print("".join(ans))
