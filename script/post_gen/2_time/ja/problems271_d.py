Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if j - a[i] >= 0 and dp[i][j - a[i]] == 1:
                dp[i + 1][j] = 1
            if j - b[i] >= 0 and dp[i][j - b[i]] == 1:
                dp[i + 1][j] = 1
    if dp[N][S] == 0:
        print('No')
        return
    print('Yes')
    ans = []
    for i in range(N):
        if dp[N - i - 1][S - a[N - i - 1]] == 1:
            ans.append('H')
            S -= a[N - i - 1]
        else:
            ans.append('T')
            S -= b[N - i - 1]
    print(''.join(ans))

=======
Suggestion 2

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())

    # dp[i][j] := i 枚目までのカードからなる部分集合で、表になっているカードの面の和が j になるようにカードを置くことができるか
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
        ans = ''
        j = S
        for i in range(N, 0, -1):
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans += 'H'
                j -= a[i - 1]
            else:
                ans += 'T'
                j -= b[i - 1]
        print(ans[::-1])
    else:
        print('No')

=======
Suggestion 3

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if dp[i][j]:
                if j + a[i] <= S:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= S:
                    dp[i+1][j+b[i]] = True
    if dp[N][S]:
        print("Yes")
        ans = ""
        while N > 0:
            if dp[N-1][S-a[N-1]]:
                ans += "H"
                S -= a[N-1]
            else:
                ans += "T"
                S -= b[N-1]
            N -= 1
        print(ans[::-1])
    else:
        print("No")

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
    for i in range(1, N + 1):
        for j in range(S + 1):
            if j >= A[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]
            if j >= B[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - B[i - 1]]
    if dp[N][S]:
        print("Yes")
        ans = []
        i = N
        j = S
        while i > 0:
            if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                ans.append("H")
                j -= A[i - 1]
            else:
                ans.append("T")
                j -= B[i - 1]
            i -= 1
        print("".join(ans[::-1]))
    else:
        print("No")

=======
Suggestion 5

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    dp = [[False for j in range(S+1)] for i in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j-a[i] >= 0:
                dp[i+1][j] |= dp[i][j-a[i]]
            if j-b[i] >= 0:
                dp[i+1][j] |= dp[i][j-b[i]]

    if dp[N][S]:
        print('Yes')
        ans = []
        i = N
        j = S
        while i > 0:
            if j-a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans.append('H')
                j -= a[i-1]
            else:
                ans.append('T')
                j -= b[i-1]
            i -= 1
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 6

def main():
    n, s = map(int, input().split())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] <= s:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= s:
                    dp[i + 1][j + b[i]] = True

    if dp[n][s]:
        print("Yes")
        ans = ""
        for i in range(n - 1, -1, -1):
            if dp[i][s - a[i]]:
                ans += "H"
                s -= a[i]
            else:
                ans += "T"
                s -= b[i]
        ans = ans[::-1]
        print(ans)
    else:
        print("No")

=======
Suggestion 7

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False] * (S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j < a[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = dp[i][j] or dp[i][j-a[i]]
            if j < b[i]:
                dp[i+1][j] = dp[i+1][j]
            else:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[N][S]:
        print('Yes')
        ans = []
        i = N
        j = S
        while i > 0:
            if j < a[i-1]:
                ans.append('T')
                i -= 1
            elif dp[i-1][j-a[i-1]]:
                ans.append('H')
                j -= a[i-1]
                i -= 1
            else:
                ans.append('T')
                i -= 1
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 8

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
        print('Yes')
        ans = []
        for i in range(N, 0, -1):
            if dp[i - 1][S - A[i - 1][0]]:
                S -= A[i - 1][0]
                ans.append('H')
            else:
                S -= A[i - 1][1]
                ans.append('T')
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 9

def main():
    N, S = map(int, input().split())
    A = [0 for i in range(N)]
    B = [0 for i in range(N)]
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j] = dp[i][j]
            if j >= A[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-A[i]]
            if j >= B[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-B[i]]
    if dp[N][S]:
        print("Yes")
        ans = ["" for i in range(N)]
        i = N
        j = S
        while i > 0:
            if j >= A[i-1] and dp[i-1][j-A[i-1]]:
                ans[i-1] = "H"
                j -= A[i-1]
            else:
                ans[i-1] = "T"
                j -= B[i-1]
            i -= 1
        print("".join(ans))
    else:
        print("No")

=======
Suggestion 10

def rec(i, j):
    if i == 0:
        if j == 0:
            return True
        else:
            return False
    if rec(i-1, j):
        return True
    if rec(i-1, j-a[i-1]):
        return True
    return False
