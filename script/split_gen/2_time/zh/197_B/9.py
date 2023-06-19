def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    X -= 1
    Y -= 1
    ans = 1
    for i in range(Y-1, -1, -1):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(Y+1, W):
        if S[X][i] == '#':
            break
        ans += 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == '#':
            break
        ans += 1
    for i in range(X+1, H):
        if S[i][Y] == '#':
            break
        ans += 1
    print(ans)
