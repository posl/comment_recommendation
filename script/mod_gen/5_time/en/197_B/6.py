def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 1
    for i in reversed(range(Y - 1)):
        if S[X - 1][i] == "#":
            break
        else:
            count += 1
    for i in range(Y, W):
        if S[X - 1][i] == "#":
            break
        else:
            count += 1
    for i in reversed(range(X - 1)):
        if S[i][Y - 1] == "#":
            break
        else:
            count += 1
    for i in range(X, H):
        if S[i][Y - 1] == "#":
            break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()