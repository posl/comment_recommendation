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
    for i in range(1, H):
        for j in range(1, W):
            if S[i][j] == '#' and S[i - 1][j] == '.' and S[i][j - 1] == '.':
                print(-1)
                return
    print(ans)
