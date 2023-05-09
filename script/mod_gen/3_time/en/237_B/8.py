def main():
    # input
    H, W = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]
    # compute
    # output
    for w in range(W):
        for h in range(H):
            print(A[h][w], end=' ')
        print()

if __name__ == '__main__':
    main()