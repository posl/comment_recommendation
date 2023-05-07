def main():
    H, W = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    x = [0] * W
    for j in range(W):
        for i in range(H):
            if c[i][j] == "#":
                x[j] += 1
    print(*x)
main()

if __name__ == '__main__':
    main()