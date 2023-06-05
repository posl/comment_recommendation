def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    if cnt == 0:
        print(0)
        return
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i == 0 or i == H-1 or j == 0 or j == W-1:
                    ans += 1
                else:
                    if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                        ans += 1
    print(ans)
