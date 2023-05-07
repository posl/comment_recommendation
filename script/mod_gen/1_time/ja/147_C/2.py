def main():
    N = int(input())
    A = [0] * N
    X = [[0] * N for i in range(N)]
    Y = [[0] * N for i in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            X[i][j], Y[i][j] = map(int, input().split())
    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if bit & (1 << i):
                for j in range(A[i]):
                    if Y[i][j] == 1:
                        if bit & (1 << (X[i][j] - 1)) == 0:
                            flag = False
                    else:
                        if bit & (1 << (X[i][j] - 1)) != 0:
                            flag = False
        if flag:
            ans = max(ans, bin(bit).count("1"))
    print(ans)

if __name__ == '__main__':
    main()