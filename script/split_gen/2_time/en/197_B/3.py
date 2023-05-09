def main():
    H, W, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    S = []
    for _ in range(H):
        S.append(input())
    ans = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    print(ans)
