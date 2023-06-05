Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = []
    t = []
    for i in range(H):
        s1 = []
        t1 = []
        for j in range(W):
            if S[i][j] == '#':
                s1.append(j)
            if T[i][j] == '#':
                t1.append(j)
        s.append(s1)
        t.append(t1)

    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def get_input():
    H,W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    return H,W,S,T

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_count = [0] * h
    t_count = [0] * h
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_count[i] += 1
            if t[i][j] == '#':
                t_count[i] += 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]

    for i in range(h):
        s[i].sort()
        t[i].sort()

    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = [list(x) for x in s]
    t = [list(x) for x in t]

    s = sorted(s)
    t = sorted(t)

    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 8

def main():
    # 由于题目的数据量很大，所以只能用C语言来实现了
    pass
