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

if __name__ == '__main__':
    solve()