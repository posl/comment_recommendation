def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for di, dj in ((1, 0), (0, 1)):
                ni = i + di
                nj = j + dj
                if ni >= H or nj >= W:
                    continue
                if S[ni][nj] == '#':
                    continue
                ans = max(ans, abs(i - ni) + abs(j - nj))
    print(ans + 1)
