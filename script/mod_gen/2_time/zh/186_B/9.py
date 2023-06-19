def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_A = min(min(A))
    count = 0
    for i in range(H):
        for j in range(W):
            count += A[i][j] - min_A
    print(count)

if __name__ == '__main__':
    main()