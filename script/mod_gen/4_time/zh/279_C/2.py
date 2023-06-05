def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S_count = [0]*W
    T_count = [0]*W
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S_count[j] += 1
            if T[i][j] == '#':
                T_count[j] += 1
    if S_count == T_count:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()