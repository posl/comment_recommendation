def get_result():
    H, W, X, Y = input().split()
    H = int(H)
    W = int(W)
    X = int(X)
    Y = int(Y)
    S = []
    for i in range(H):
        S.append(input())
    result = 1
    for i in range(X-2, -1, -1):
        if S[i][Y-1] == "#":
            break
        else:
            result += 1
    for i in range(X, H):
        if S[i][Y-1] == "#":
            break
        else:
            result += 1
    for i in range(Y-2, -1, -1):
        if S[X-1][i] == "#":
            break
        else:
            result += 1
    for i in range(Y, W):
        if S[X-1][i] == "#":
            break
        else:
            result += 1
    return result
