def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[int(_) for _ in input().split()] for _ in range(sum(A))]
    Y = [1 for _ in range(sum(A))]
    for i in range(N):
        for j in range(A[i]):
            X[i][j] -= 1
    for i in range(N):
        for j in range(A[i]):
            if X[i][j] == i:
                Y[i] = 0
    print(Y)

if __name__ == '__main__':
    main()