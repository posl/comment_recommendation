def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 0
    for i in range(Y-1, -1, -1):
        if S[X-1][i] == ".":
            count += 1
        else:
            break
    for i in range(Y, W):
        if S[X-1][i] == ".":
            count += 1
        else:
            break
    for i in range(X-1, -1, -1):
        if S[i][Y-1] == ".":
            count += 1
        else:
            break
    for i in range(X, H):
        if S[i][Y-1] == ".":
            count += 1
        else:
            break
    print(count)
main()
