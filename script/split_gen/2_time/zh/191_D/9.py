def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ans += 1
    if ans == 0:
        print(0)
        return
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i + 1][j] == '.' and S[i][j - 1] == '.' and S[i][j + 1] == '.':
                ans += 1
    if ans == 0:
        print(1)
        return
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and ((S[i - 1][j] == '.' and S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i][j + 1] == '.') or (S[i - 1][j] == '#' and S[i + 1][j] == '.' and S[i][j - 1] == '.' and S[i][j + 1] == '#') or (S[i - 1][j] == '#' and S[i + 1][j] == '#' and S[i][j - 1] == '.' and S[i][j + 1] == '.') or (S[i - 1][j] == '.' and S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i][j + 1] == '#')):
                ans += 1
    if ans == 0:
        print(2)
        return
    ans = 0
    for i in range(1, H - 1):
        for j in range(1, W - 1):
            if S[i][j] == '#' and ((S[i - 1][j] == '.' and S[i + 1][j] == '.' and S[i][j - 1
