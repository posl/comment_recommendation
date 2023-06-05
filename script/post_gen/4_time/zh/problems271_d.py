Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, s = map(int, input().split())
    cards = []
    for _ in range(n):
        a, b = map(int, input().split())
        cards.append((a, b))
    # print(cards)
    # print(n, s)
    for i in range(2 ** n):
        # print(i)
        total = 0
        for j in range(n):
            if (i >> j) & 1:
                total += cards[j][0]
            else:
                total += cards[j][1]
        if total == s:
            print("Yes")
            for j in range(n):
                if (i >> j) & 1:
                    print("H", end="")
                else:
                    print("T", end="")
            print()
            return
    print("No")

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def dfs(i, sum):
    if i == n:
        return sum == s
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False

n, s = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

=======
Suggestion 4

def main():
    n, s = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j+a[i][0] <= s:
                    dp[i+1][j+a[i][0]] = True
                if j+a[i][1] <= s:
                    dp[i+1][j+a[i][1]] = True
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = ""
    for i in range(n-1, 0, -1):
        if s-a[i-1][0] >= 0 and dp[i][s-a[i-1][0]]:
            ans += "H"
            s -= a[i-1][0]
        else:
            ans += "T"
            s -= a[i-1][1]
    print(ans[::-1])

=======
Suggestion 5

def solve():
    N, S = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    # print(N, S, AB)
    if any(a + b == S for a, b in AB):
        print('Yes')
        for a, b in AB:
            if a + b == S:
                print('H', end='')
            else:
                print('T', end='')
        print()
        return
    else:
        print('No')
        return

=======
Suggestion 6

def main():
    n, s = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) < s:
        print('No')
        return
    else:
        print('Yes')
    sum_a = 0
    sum_b = 0
    for i in range(n):
        if sum_a + a[i] < s:
            print('H', end='')
            sum_a += a[i]
        else:
            print('T', end='')
            sum_b += b[i]
    print()
    return

=======
Suggestion 7

def dfs(i, sum):
    if i == N:
        return sum == S
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + A[i]):
        return True
    return False

N, S = map(int, input().split())
A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)

=======
Suggestion 8

def f(n,s,a):
    if n==0: return s==0
    if f(n-1,s-a[n-1]): return True
    if f(n-1,s): return True
    return False

=======
Suggestion 9

def solve():
    # N:卡片数目，S:目标和
    N, S = map(int, input().split())
    # a:正面数字，b:背面数字
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    # 使用动态规划
    # dp[i][j]:表示前i张牌中，能否组成和j
    # dp[i][j] = dp[i-1][j-a[i]] or dp[i-1][j-b[i]]
    dp = [[False] * (S+1) for i in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= a[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-a[i]]
            if j >= b[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[N][S]:
        print("Yes")
        # 从后往前推，找出是哪张牌的正面或者背面
        ans = ""
        for i in range(N-1, -1, -1):
            if S >= a[i] and dp[i][S-a[i]]:
                ans += "H"
                S -= a[i]
            else:
                ans += "T"
                S -= b[i]
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 10

def solve():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for s in range(S + 1):
            if dp[i][s]:
                dp[i + 1][s] = True
            if s - cards[i][0] >= 0 and dp[i][s - cards[i][0]]:
                dp[i + 1][s] = True
            if s - cards[i][1] >= 0 and dp[i][s - cards[i][1]]:
                dp[i + 1][s] = True

    if not dp[N][S]:
        print('No')
        return

    print('Yes')
    ans = []
    s = S
    for i in range(N - 1, -1, -1):
        if s - cards[i][0] >= 0 and dp[i][s - cards[i][0]]:
            ans.append('H')
            s -= cards[i][0]
        elif s - cards[i][1] >= 0 and dp[i][s - cards[i][1]]:
            ans.append('T')
            s -= cards[i][1]
        else:
            assert False
    print(''.join(reversed(ans)))
