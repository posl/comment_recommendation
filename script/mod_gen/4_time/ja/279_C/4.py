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

if __name__ == '__main__':
    solve()