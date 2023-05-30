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
