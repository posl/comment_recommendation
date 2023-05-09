def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = [[A[i], B[i], C[i], i + 1] for i in range(N)]
    D.sort(key=lambda x: (-x[0], x[3]))
    D.sort(key=lambda x: (-x[2], x[3]))
    D.sort(key=lambda x: (-x[1], x[3]))
    for i in range(X + Y + Z):
        print(D[i][3])

if __name__ == '__main__':
    main()