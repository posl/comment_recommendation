def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    black = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                black += 1
    if black == H + W - 1:
        print(2)
        return
    if black == H + W - 2:
        print(3)
        return
    if black == H + W - 3:
        print(4)
        return
    print(1)
    return

if __name__ == '__main__':
    main()