def problem():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min:
                min = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min
    print(ans)
problem()

if __name__ == '__main__':
    problem()