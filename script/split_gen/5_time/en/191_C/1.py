def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                continue
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                ans += 1
                continue
            if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                ans += 1
    print(ans)
