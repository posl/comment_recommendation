def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#' and S[i+1][j+1] == '#':
                ans += 1
    print(ans)
