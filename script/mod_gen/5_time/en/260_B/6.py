def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_B = []
    for i in range(N):
        A_B.append([A[i], B[i], i+1])
    A_B.sort(key=lambda x: x[2])
    A_B.sort(key=lambda x: x[1], reverse=True)
    A_B.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(A_B[i][2])
    for i in range(Y):
        print(A_B[X+i][2])
    for i in range(Z):
        print(A_B[X+Y+i][2])

if __name__ == '__main__':
    main()