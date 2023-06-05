def problem197_b():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 1
    for i in range(X - 1, -1, -1):
        if S[i][Y - 1] == '#':
            break
        else:
            count += 1
    for i in range(X, H):
        if S[i][Y - 1] == '#':
            break
        else:
            count += 1
    for j in range(Y - 1, -1, -1):
        if S[X - 1][j] == '#':
            break
        else:
            count += 1
    for j in range(Y, W):
        if S[X - 1][j] == '#':
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    problem197_b()