def solve():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in range(X + 1, H):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(X - 1, -1, -1):
        if S[i][Y] == '.':
            ans += 1
        else:
            break
    for i in range(Y + 1, W):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    for i in range(Y - 1, -1, -1):
        if S[X][i] == '.':
            ans += 1
        else:
            break
    print(ans)
