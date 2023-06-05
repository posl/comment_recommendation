def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(W):
        B.append([])
        for j in range(H):
            B[i].append(A[j][i])
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(B[i][j])
            else:
                print(B[i][j], end=' ')

if __name__ == '__main__':
    main()