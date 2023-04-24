Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) < S:
        print("No")
        return
    if sum(b) > S:
        print("No")
        return
    dp = [[False for j in range(S+1)] for i in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for j in range(S+1):
            if j - a[i-1] >= 0:
                dp[i][j] = dp[i-1][j-a[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    if dp[N][S]:
        print("Yes")
        ans = []
        j = S
        for i in range(N, 0, -1):
            if j - a[i-1] >= 0:
                if dp[i-1][j-a[i-1]]:
                    ans.append("H")
                    j = j - a[i-1]
                else:
                    ans.append("T")
            else:
                ans.append("T")
        print("".join(ans[::-1]))
    else:
        print("No")

=======
Suggestion 2

def main():
    N, S = map(int, input().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] |= dp[i][j - A[i]]
            if j - B[i] >= 0:
                dp[i + 1][j] |= dp[i][j - B[i]]
    if dp[N][S]:
        print('Yes')
        ans = ''
        for i in range(N - 1, -1, -1):
            if S - A[i] >= 0 and dp[i][S - A[i]]:
                ans += 'H'
                S -= A[i]
            else:
                ans += 'T'
                S -= B[i]
        print(ans[::-1])
    else:
        print('No')

=======
Suggestion 3

def solve():
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
                dp[i + 1][j] |= dp[i][j - A[i]]
            if j - B[i] >= 0:
                dp[i + 1][j] |= dp[i][j - B[i]]
    if dp[N][S]:
        print("Yes")
        i = N
        j = S
        ans = ""
        while i > 0:
            if j - A[i - 1] >= 0 and dp[i - 1][j - A[i - 1]]:
                ans += "H"
                j -= A[i - 1]
            else:
                ans += "T"
                j -= B[i - 1]
            i -= 1
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 4

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # dp[i][j] := i枚目まで見たときに、jを作ることができるかどうか
    dp = [[False for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for j in range(S+1):
            if dp[i-1][j]:
                dp[i][j] = True
                if j+a[i-1] <= S:
                    dp[i][j+a[i-1]] = True
                if j+b[i-1] <= S:
                    dp[i][j+b[i-1]] = True

    if dp[N][S]:
        print('Yes')
        ans = ''
        j = S
        for i in range(N, 0, -1):
            if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans += 'H'
                j -= a[i-1]
            else:
                ans += 'T'
                j -= b[i-1]
        print(ans[::-1])
    else:
        print('No')

=======
Suggestion 5

def main():
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
        ans = ""
        j = S
        for i in range(N, 0, -1):
            if j - A[i - 1][0] >= 0 and dp[i - 1][j - A[i - 1][0]]:
                ans += "H"
                j -= A[i - 1][0]
            else:
                ans += "T"
                j -= A[i - 1][1]
        print(ans[::-1])
    else:
        print("No")

=======
Suggestion 6

def main():
    N, S = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] = dp[i][j] or dp[i][j - A[i][0]] or dp[i][j - A[i][1]]
    if dp[N][S]:
        print('Yes')
        ans = []
        j = S
        for i in range(N, 0, -1):
            if dp[i - 1][j - A[i - 1][0]]:
                ans.append('H')
                j -= A[i - 1][0]
            elif dp[i - 1][j - A[i - 1][1]]:
                ans.append('T')
                j -= A[i - 1][1]
            else:
                ans.append('H')
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 7

def main():
    n,s = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int, input().split())
    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j-a[i]>=0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-a[i]]
            if j-b[i]>=0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[n][s]:
        print('Yes')
        ans = ''
        i = n
        j = s
        while i>0:
            if j-a[i-1]>=0 and dp[i-1][j-a[i-1]]:
                ans += 'H'
                j -= a[i-1]
            else:
                ans += 'T'
                j -= b[i-1]
            i -= 1
        print(ans[::-1])
    else:
        print('No')

=======
Suggestion 8

def solve(N, S, A, B):
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            if j >= A[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-A[i]])
            if j >= B[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-B[i]])
    if dp[N][S] == 0:
        print("No")
    else:
        print("Yes")
        ans = ""
        for i in range(N):
            if S >= A[N-i-1] and dp[N-i-1][S-A[N-i-1]] == 1:
                ans += "H"
                S -= A[N-i-1]
            else:
                ans += "T"
                S -= B[N-i-1]
        print(ans)

=======
Suggestion 9

def solve(n, s, a, b):
    for i in range(1 << n):
        t = 0
        for j in range(n):
            if (i >> j) & 1:
                t += a[j]
            else:
                t += b[j]
        if t == s:
            return "Yes" + "

" + "".join(["T" if (i >> j) & 1 else "H" for j in range(n)])
    return "No"

n, s = map(int, input().split())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
print(solve(n, s, a, b))

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))

n, s = read_ints()

cards = []
for i in range(n):
    a, b = read_ints()
    cards.append((a, b))
