Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem218_c():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(input()))
    for i in range(n):
        t.append(list(input()))

    if s == t:
        print('Yes')
        return

    for i in range(3):
        t = rotate(t)
        if s == t:
            print('Yes')
            return

    print('No')

=======
Suggestion 2

def rotate90(S):
    N = len(S)
    T = [['' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            T[j][N-1-i] = S[i][j]
    return T

=======
Suggestion 3

def check(S,T):
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] != T[i][j]:
                return False
    return True

=======
Suggestion 4

def rotate90(s):
    return [''.join(x) for x in zip(*s[::-1])]

=======
Suggestion 5

def rotate90(s):
    s2 = s[:]
    for i in range(len(s)):
        for j in range(len(s)):
            s2[j][len(s)-i-1] = s[i][j]
    return s2

=======
Suggestion 6

def rotate90(data):
    # 逆时针旋转90度
    n = len(data)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = data[j][n - i - 1]
    return res

=======
Suggestion 7

def is_same(s, t):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] != t[i][j]:
                return False
    return True

=======
Suggestion 8

def rotate90(grid):
    n = len(grid)
    new_grid = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[j][n - i - 1] = grid[i][j]
    return new_grid

=======
Suggestion 9

def rotate_90(li):
    li_new = []
    for i in range(len(li)):
        li_new.append([])
        for j in range(len(li)):
            li_new[i].append(li[len(li)-1-j][i])
    return li_new
