Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - a[i] >= 0:
                dp[i + 1][j] |= dp[i][j - a[i]]
            if j - b[i] >= 0:
                dp[i + 1][j] |= dp[i][j - b[i]]
    if dp[N][S]:
        ans = []
        j = S
        for i in range(N, 0, -1):
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans.append('H')
                j -= a[i - 1]
            else:
                ans.append('T')
                j -= b[i - 1]
        print('Yes')
        print(''.join(ans[::-1]))
    else:
        print('No')

=======
Suggestion 2

def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j + a[i] <= S:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= S:
                    dp[i+1][j+b[i]] = True
    if dp[N][S]:
        print("Yes")
        ans = ""
        i = N
        j = S
        while i > 0:
            if j - a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans = "H" + ans
                j -= a[i-1]
            else:
                ans = "T" + ans
                j -= b[i-1]
            i -= 1
        print(ans)
    else:
        print("No")

=======
Suggestion 3

def main():
    N, S = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i][j] | dp[i][j - A[i]]
            else:
                dp[i + 1][j] = dp[i][j]
            if j - B[i] >= 0:
                dp[i + 1][j] = dp[i][j] | dp[i][j - B[i]]
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[N][S]:
        print('Yes')
        ans = []
        for i in range(N - 1, -1, -1):
            if S - A[i] >= 0:
                if dp[i][S - A[i]]:
                    ans.append('H')
                    S -= A[i]
                    continue
            if S - B[i] >= 0:
                if dp[i][S - B[i]]:
                    ans.append('T')
                    S -= B[i]
                    continue
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
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 0:
                continue
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] = 1
            if j + B[i] <= S:
                dp[i + 1][j + B[i]] = 2
    if dp[N][S] == 0:
        print("No")
        return
    ans = ""
    now = S
    for i in range(N, 0, -1):
        if dp[i][now] == 1:
            ans += "H"
            now -= A[i - 1]
        else:
            ans += "T"
            now -= B[i - 1]
    print("Yes")
    print(ans[::-1])

=======
Suggestion 5

def main():
    N, S = map(int, input().split())
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j-a[i]>=0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            if j-b[i]>=0 and dp[i][j-b[i]]:
                dp[i+1][j] = True
    if dp[N][S]:
        print('Yes')
        ans = ''
        i = N
        j = S
        while i>0:
            if j-a[i-1]>=0 and dp[i-1][j-a[i-1]]:
                ans = 'H' + ans
                j -= a[i-1]
            else:
                ans = 'T' + ans
                j -= b[i-1]
            i -= 1
        print(ans)
    else:
        print('No')

=======
Suggestion 6

def main():
    N, S = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # dp[i][j]: i枚目までのカードを使ってjを作ることができるかどうか
    dp = [[False for i in range(S+1)] for j in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(S+1):
            if j-a[i] >= 0 and dp[i][j-a[i]]:
                dp[i+1][j] = True
            if j-b[i] >= 0 and dp[i][j-b[i]]:
                dp[i+1][j] = True

    if dp[N][S]:
        print("Yes")
        ans = ""
        for i in range(N-1, -1, -1):
            if S-a[i] >= 0 and dp[i][S-a[i]]:
                ans += "H"
                S -= a[i]
            else:
                ans += "T"
                S -= b[i]
        print(ans[::-1])
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

    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                if j + a[i] <= S:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= S:
                    dp[i + 1][j + b[i]] = True

    if dp[N][S]:
        print("Yes")
        ans = []
        i = N
        j = S
        while i > 0:
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans.append("H")
                j -= a[i - 1]
            else:
                ans.append("T")
                j -= b[i - 1]
            i -= 1
        ans.reverse()
        print("".join(ans))
    else:
        print("No")

=======
Suggestion 8

def main():
    N, S = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i][0]:
                dp[i + 1][j] = dp[i][j - A[i][0]] or dp[i][j]
            if j >= A[i][1]:
                dp[i + 1][j] = dp[i][j - A[i][1]] or dp[i][j]
    if dp[N][S]:
        print('Yes')
        T = ['H' if dp[i][S - A[i][0]] else 'T' for i in range(N)]
        print(''.join(T))
    else:
        print('No')

=======
Suggestion 9

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
        for i in reversed(range(N)):
            if S - A[i][0] >= 0 and dp[i][S - A[i][0]]:
                ans.append('H')
                S -= A[i][0]
            else:
                ans.append('T')
                S -= A[i][1]
        print(''.join(reversed(ans)))
    else:
        print('No')

=======
Suggestion 10

def main():
    # 入力
    N,S = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    # 1枚目の選択
    for i in range(2**N):
        # 2進数に変換
        i = bin(i)[2:].zfill(N)
        # 各カードの表と裏の和を計算
        sum_a = 0
        sum_b = 0
        for j in range(N):
            if i[j] == '0':
                sum_a += a[j]
            else:
                sum_b += b[j]
        # 和がSと一致する場合
        if sum_a + sum_b == S:
            print('Yes')
            print(i)
            return
    print('No')
    return
