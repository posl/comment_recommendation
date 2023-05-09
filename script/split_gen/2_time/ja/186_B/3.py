def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j] - min
    print(sum)
    return 0
