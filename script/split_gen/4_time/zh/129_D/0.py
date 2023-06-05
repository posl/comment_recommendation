def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                cnt = 1
                for k in range(i - 1, -1, -1):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(i + 1, H):
                    if S[k][j] == '#':
                        break
                    cnt += 1
                for k in range(j - 1, -1, -1):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                for k in range(j + 1, W):
                    if S[i][k] == '#':
                        break
                    cnt += 1
                ans = max(ans, cnt)
    print(ans)
