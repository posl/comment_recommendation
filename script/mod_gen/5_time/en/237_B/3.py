def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(A[j][i])
            else:
                print(A[j][i], end=" ")

if __name__ == '__main__':
    main()