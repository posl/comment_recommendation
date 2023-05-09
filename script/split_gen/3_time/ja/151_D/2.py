def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for k in range(i + 1, H):
                for l in range(j + 1, W):
                    if S[k][l] == '#':
                        continue
                    ans = max(ans, abs(i - k) + abs(j - l) + 1)
    print(ans)
