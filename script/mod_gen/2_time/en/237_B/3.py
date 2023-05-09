def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]
    for row in B:
        print(*row)

if __name__ == '__main__':
    main()