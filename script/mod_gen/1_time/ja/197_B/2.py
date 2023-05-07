def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    X -= 1
    Y -= 1
    count = 1
    for i in range(X + 1, H):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(X - 1, -1, -1):
        if S[i][Y] == ".":
            count += 1
        else:
            break
    for i in range(Y + 1, W):
        if S[X][i] == ".":
            count += 1
        else:
            break
    for i in range(Y - 1, -1, -1):
        if S[X][i] == ".":
            count += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    main()