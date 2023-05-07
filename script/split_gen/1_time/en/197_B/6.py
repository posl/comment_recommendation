def main():
    H, W, X, Y = [int(i) for i in input().split()]
    S = [input() for _ in range(H)]
    ans = 1
    for i in range(X - 1, 0, -1):
        if S[i - 1][Y - 1] == '#':
            break
        ans += 1
    for i in range(X + 1, H + 1):
        if S[i - 1][Y - 1] == '#':
            break
        ans += 1
    for j in range(Y - 1, 0, -1):
        if S[X - 1][j - 1] == '#':
            break
        ans += 1
    for j in range(Y + 1, W + 1):
        if S[X - 1][j - 1] == '#':
            break
        ans += 1
    print(ans)
