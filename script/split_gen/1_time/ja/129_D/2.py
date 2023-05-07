def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for h in range(H):
        cnt = 0
        for w in range(W):
            if S[h][w] == '#':
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt += 1
        ans = max(ans, cnt)
    for w in range(W):
        cnt = 0
        for h in range(H):
            if S[h][w] == '#':
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
