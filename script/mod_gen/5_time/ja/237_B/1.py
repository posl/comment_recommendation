def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    B = []
    for j in range(W):
        B.append([])
        for i in range(H):
            B[j].append(A[i][j])
    for j in range(W):
        print(' '.join(map(str, B[j])))

if __name__ == '__main__':
    main()