def main():
    N,Q = map(int,input().split())
    # 隣接行列の初期化
    matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        T,A,B = map(int,input().split())
        if T == 1:
            matrix[A-1][B-1] = 1
        elif T == 2:
            matrix[B-1][A-1] = 1
            for j in range(N):
                if matrix[j][A-1] == 1:
                    matrix[j][B-1] = 1
        else:
            if matrix[A-1][B-1] == 1:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()