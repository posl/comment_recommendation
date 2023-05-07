def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    count = 1
    for i in range(1, H):
        if S[X-1-i][Y-1] == "#":
            break
        count += 1
    for i in range(1, H):
        if S[X-1+i][Y-1] == "#":
            break
        count += 1
    for i in range(1, W):
        if S[X-1][Y-1-i] == "#":
            break
        count += 1
    for i in range(1, W):
        if S[X-1][Y-1+i] == "#":
            break
        count += 1
    print(count)

if __name__ == '__main__':
    main()