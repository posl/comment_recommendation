def main():
    H, W, X, Y = map(int, input().split())
    S = [list(input()) for i in range(H)]
    count = 1
    for i in range(X - 2, -1, -1):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        count += 1
    for i in range(Y - 2, -1, -1):
        if S[X - 1][i] == '#':
            break
        count += 1
    for i in range(Y, W):
        if S[X - 1][i] == '#':
            break
        count += 1
    print(count)
