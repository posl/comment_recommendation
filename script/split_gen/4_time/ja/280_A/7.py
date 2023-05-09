def solve():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                ans += 1
    print(ans)
