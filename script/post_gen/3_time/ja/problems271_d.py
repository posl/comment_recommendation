Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    #dp[i][j] i枚目まで見たときにjの合計ができるか
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 1:
                if a[i] + j <= S:
                    dp[i + 1][a[i] + j] = 1
                if b[i] + j <= S:
                    dp[i + 1][b[i] + j] = 1
    if dp[N][S] == 1:
        print("Yes")
        ans = ""
        for i in range(N):
            if dp[N - i - 1][S - a[N - i - 1]] == 1:
                ans += "H"
                S -= a[N - i - 1]
            else:
                ans += "T"
                S -= b[N - i - 1]
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 2

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())

    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(S+1):
            if j - a[i] >= 0:
                dp[i+1][j] += dp[i][j-a[i]]
            if j - b[i] >= 0:
                dp[i+1][j] += dp[i][j-b[i]]

    if dp[N][S] == 0:
        print("No")
    else:
        print("Yes")
        ans = []
        j = S
        for i in range(N, 0, -1):
            if dp[i-1][j-a[i-1]] == 1:
                ans.append("H")
                j -= a[i-1]
            else:
                ans.append("T")
                j -= b[i-1]
        print("".join(ans[::-1]))

=======
Suggestion 3

def main():
    N, S = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[False] * (S + 1) for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
            if j >= B[i] and dp[i][j - B[i]]:
                dp[i + 1][j] = True
    if dp[N][S]:
        print('Yes')
        ans = []
        i = N
        j = S
        while i > 0:
            if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                ans.append('H')
                j -= A[i - 1]
            else:
                ans.append('T')
                j -= B[i - 1]
            i -= 1
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 4

def main():
    N, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - A[i]]
            if j - B[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - B[i]]
    if dp[N][S]:
        print("Yes")
        ans = ""
        for i in reversed(range(N)):
            if S - A[i] >= 0 and dp[i][S - A[i]]:
                ans += "H"
                S -= A[i]
            else:
                ans += "T"
                S -= B[i]
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 5

def main():
    N, S = map(int, input().split())
    a = [None] * N
    b = [None] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] <= S:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= S:
                    dp[i + 1][j + b[i]] = True
    if dp[N][S]:
        print('Yes')
        ans = [None] * N
        for i in range(N, 0, -1):
            if S - a[i - 1] >= 0 and dp[i - 1][S - a[i - 1]]:
                ans[i - 1] = 'H'
                S -= a[i - 1]
            else:
                ans[i - 1] = 'T'
                S -= b[i - 1]
        print(''.join(ans))
    else:
        print('No')

=======
Suggestion 6

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
            if j - a[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - a[i]]
            if j - b[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j] or dp[i][j - b[i]]
    if dp[N][S]:
        print("Yes")
        ans = []
        for i in range(N):
            if S - a[N - i - 1] >= 0 and dp[N - i - 1][S - a[N - i - 1]]:
                ans.append("H")
                S -= a[N - i - 1]
            else:
                ans.append("T")
                S -= b[N - i - 1]
        print("".join(ans))
    else:
        print("No")

=======
Suggestion 7

def main():
    N,S=map(int,input().split())
    a,b=[],[]
    for i in range(N):
        a_i,b_i=map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    dp=[[0 for j in range(S+1)] for i in range(N+1)]
    dp[0][0]=1
    for i in range(N):
        for j in range(S+1):
            if j-a[i]>=0:
                dp[i+1][j]=max(dp[i][j],dp[i][j-a[i]]+b[i])
            else:
                dp[i+1][j]=max(dp[i][j],dp[i][j]+b[i])
    if dp[N][S]==S:
        print("Yes")
        ans=""
        for i in range(N):
            if dp[N-i-1][S-a[N-i-1]]==S-b[N-i-1]:
                ans="H"+ans
                S-=a[N-i-1]
            else:
                ans="T"+ans
        print(ans)
    else:
        print("No")

=======
Suggestion 8

def main():
    # 入力
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)
    # 処理
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - a[i] >= 0 and dp[i][j - a[i]]:
                dp[i + 1][j] = True
            if j - b[i] >= 0 and dp[i][j - b[i]]:
                dp[i + 1][j] = True
    # 出力
    if dp[N][S]:
        print("Yes")
        ans = ""
        i = N
        j = S
        while i > 0:
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans = "H" + ans
                j -= a[i - 1]
            else:
                ans = "T" + ans
                j -= b[i - 1]
            i -= 1
        print(ans)
    else:
        print("No")

=======
Suggestion 9

def main():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        cards.append(list(map(int, input().split())))
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j - cards[i][0] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][0]]
            if j - cards[i][1] >= 0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-cards[i][1]]
    if dp[N][S]:
        print("Yes")
        ans = []
        for i in range(N-1, -1, -1):
            if S - cards[i][0] >= 0 and dp[i][S-cards[i][0]]:
                ans.append("H")
                S -= cards[i][0]
            else:
                ans.append("T")
                S -= cards[i][1]
        print("".join(ans[::-1]))
    else:
        print("No")

=======
Suggestion 10

def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j] = i枚目までのカードでjを作れるか
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j - cards[i][0] >= 0 and dp[i][j - cards[i][0]]:
                dp[i + 1][j] = True
            if j - cards[i][1] >= 0 and dp[i][j - cards[i][1]]:
                dp[i + 1][j] = True

    if not dp[n][s]:
        print("No")
        return

    print("Yes")
    ans = ["" for _ in range(n)]
    i = n
    j = s
    while i > 0:
        if j - cards[i - 1][0] >= 0 and dp[i - 1][j - cards[i - 1][0]]:
            ans[i - 1] = "H"
            j -= cards[i - 1][0]
        else:
            ans[i - 1] = "T"
            j -= cards[i - 1][1]
        i -= 1
    print("".join(ans))
