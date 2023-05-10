def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    count = 0
    for i in range(H):
        for j in range(W):
            count += A[i][j] - min
    print(count)

if __name__ == '__main__':
    main()