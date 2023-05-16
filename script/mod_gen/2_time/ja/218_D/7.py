def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: x[0])
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            # ここで、A[i][0] <= A[j][0] と仮定する
            # A[i][0] = A[j][0] なら、A[i][1] < A[j][1] と仮定する
            # このとき、A[i][0] = A[j][0] かつ A[i][1] = A[j][1] はありえない
            # なぜなら、点の座標は全て整数であるから
            # したがって、A[i][0] = A[j][0] かつ A[i][1] = A[j][1] はありえない
            # したがって、A[i][0] = A[j][0] なら、A[i][1] < A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[i][1] + (A[j][0] - A[i][0]) == A[j][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[j][1] - (A[j][0] - A[i][0]) == A[i][1] である
            # したがって、A[i][0] <= A[j][0] かつ A[i][1] < A[j][1] かつ A[i][0] <= A[j][1] - (A[j][0] - A[i][0]) <= A[j][0] である

if __name__ == '__main__':
    main()