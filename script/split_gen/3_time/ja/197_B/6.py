def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    #print(H, W, X, Y)
    #print(S)
    #print(S[X])
    #print(S[X][Y])
    count = 0
    if S[X][Y] == ".":
        count += 1
    #print(count)
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(Y-1, -1, -1):
        if S[X][i] == "#":
            break
        else:
            count += 1
    #print(count)
    for i in range(Y+1, W):
        if S[X][i] == "#":
            break
        else:
            count += 1
    print(count)
