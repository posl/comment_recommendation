def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h == 0 and w == 0:
                continue
            if h == 0:
                A[h][w] += A[h][w - 1]
                continue
            if w == 0:
                A[h][w] += A[h - 1][w]
                continue
            A[h][w] += min(A[h - 1][w], A[h][w - 1])
    print('Yes' if A[H - 1][W - 1] % 2 == 0 else 'No')

if __name__ == '__main__':
    main()