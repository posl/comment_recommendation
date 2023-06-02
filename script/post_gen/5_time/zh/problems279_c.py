Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]

    s = [list(x) for x in zip(*s)]
    t = [list(x) for x in zip(*t)]

    s.sort()
    t.sort()

    print("Yes" if s == t else "No")

=======
Suggestion 3

def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    return H, W, S, T

=======
Suggestion 4

def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    return H, W, S, T

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_col = [0]*w
    s_row = [0]*h
    t_col = [0]*w
    t_row = [0]*h
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_col[j] += 1
                s_row[i] += 1
            if t[i][j] == '#':
                t_col[j] += 1
                t_row[i] += 1
    if s_col == t_col and s_row == t_row:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    def rotate(S):
        return [''.join(x) for x in zip(*S[::-1])]

    for _ in range(4):
        S = rotate(S)
        if S == T:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    def rotate(S):
        return [''.join([S[i][j] for i in range(H)]) for j in range(W)]

    def check(S, T):
        return S == T or rotate(S) == T or rotate(rotate(S)) == T or rotate(rotate(rotate(S))) == T

    print("Yes" if check(S, T) else "No")

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = ''.join(sorted(s[i]))
        t[i] = ''.join(sorted(t[i]))
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                exit()
    print('Yes')
