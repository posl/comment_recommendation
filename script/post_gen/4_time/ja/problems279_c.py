Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    #a = int(input())
    # スペース区切りの整数の入力
    #b, c = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    #print(S)
    #print(T)
    S_count = []
    for i in range(W):
        S_count.append([0,0])
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                S_count[j][0] += 1
            else:
                S_count[j][1] += 1
    #print(S_count)
    T_count = []
    for i in range(W):
        T_count.append([0,0])
    for i in range(H):
        for j in range(W):
            if T[i][j] == "#":
                T_count[j][0] += 1
            else:
                T_count[j][1] += 1
    #print(T_count)
    S_count.sort()
    T_count.sort()
    #print(S_count)
    #print(T_count)
    for i in range(W):
        if S_count[i] != T_count[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S_count = [[0] * W for _ in range(H)]
    T_count = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S_count[i][j] = 1
            if T[i][j] == '#':
                T_count[i][j] = 1
    for i in range(H):
        for j in range(1, W):
            S_count[i][j] += S_count[i][j - 1]
            T_count[i][j] += T_count[i][j - 1]
    for i in range(1, H):
        for j in range(W):
            S_count[i][j] += S_count[i - 1][j]
            T_count[i][j] += T_count[i - 1][j]
    for i in range(H):
        for j in range(W):
            if S_count[i][j] != T_count[i][j]:
                print('No')
                return
    print('Yes')

=======
Suggestion 3

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = [0] * H
    t = [0] * H
    for i in range(H):
        s[i] = [0] * W
        t[i] = [0] * W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s[i][j] = 1
            else:
                s[i][j] = 0
            if T[i][j] == '#':
                t[i][j] = 1
            else:
                t[i][j] = 0
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    S = [list(s) for s in S]
    T = [list(t) for t in T]

    s_cnt = [0] * W
    t_cnt = [0] * W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s_cnt[j] += 1
            if T[i][j] == '#':
                t_cnt[j] += 1

    for i in range(H):
        if s_cnt != t_cnt:
            return False

    s_cnt = [0] * H
    t_cnt = [0] * H
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                s_cnt[i] += 1
            if T[i][j] == '#':
                t_cnt[i] += 1

    for i in range(H):
        if s_cnt != t_cnt:
            return False

    return True

print('Yes' if solve() else 'No')

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    S_count = []
    for i in range(H):
        S_count.append(S[i].count('#'))

    T_count = []
    for i in range(H):
        T_count.append(T[i].count('#'))

    if S_count == T_count:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_count = [0 for _ in range(w)]
    t_count = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_count[j] += 1
            if t[i][j] == '#':
                t_count[j] += 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = sorted(S)
    T = sorted(T)
    for i in range(H):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    from collections import Counter

    s_cnt = Counter()
    t_cnt = Counter()

    for i in range(H):
        s_cnt[S[i]] += 1
        t_cnt[T[i]] += 1

    if s_cnt != t_cnt:
        print("No")
        exit()

    s = [[] for _ in range(H)]
    t = [[] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            s[i].append(S[i][j])
            t[i].append(T[i][j])

    s.sort()
    t.sort()

    for i in range(H):
        if s[i] != t[i]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 9

def solve():
    H,W = list(map(int,input().split()))
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    S_count = [0]*H
    T_count = [0]*H
    for i in range(H):
        S_count[i] = S[i].count("#")
        T_count[i] = T[i].count("#")
    if S_count != T_count:
        print("No")
        return
    for i in range(H):
        if S[i] != T[i]:
            if S[i][0] == "#":
                S[i] = S[i][::-1]
            if S[i] != T[i]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 10

def check(S, T):
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print('Yes')
    else:
        print('No')
