def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    X -= 1
    Y -= 1
    count = 1
    for i in range(X-1, -1, -1):
        if S[i][Y] == "#":
            break
        count += 1
    for i in range(X+1, H):
        if S[i][Y] == "#":
            break
        count += 1
    for j in range(Y-1, -1, -1):
        if S[X][j] == "#":
            break
        count += 1
    for j in range(Y+1, W):
        if S[X][j] == "#":
            break
        count += 1
    print(count)
main()

if __name__ == '__main__':
    main()