def main():
    # H, W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H, W = 5, 5
    S = [
        '.....',
        '.###.',
        '.###.',
        '.###.',
        '.....'
    ]
    # print(H, W, S)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    print(ans)
