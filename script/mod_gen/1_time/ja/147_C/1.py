def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][j] = x
            Y[i][j] = y
    for i in range(2 ** N):
        bit = bin(i)[2:].zfill(N)
        flag = True
        for j in range(N):
            if bit[j] == '1':
                for k in range(A[j]):
                    if bit[X[j][k] - 1] == '1' and Y[j][k] == 0:
                        flag = False
                    elif bit[X[j][k] - 1] == '0' and Y[j][k] == 1:
                        flag = False
        if flag:
            print(bit.count('1'))

if __name__ == '__main__':
    main()