def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    s = [[0]*W for _ in range(H)]
    t = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            s[i][j] = S[i][j]
            t[i][j] = T[i][j]
    s.sort()
    t.sort()
    for i in range(H):
        for j in range(W):
            if s[i][j] != t[i][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    solve()