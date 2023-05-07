def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    B = [int(input()) for _ in range(N)]
    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    A[i][j] = 0
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == 0:
            print('Yes')
            return
        if A[0][i] == A[1][i] == A[2][i] == 0:
            print('Yes')
            return
    if A[0][0] == A[1][1] == A[2][2] == 0:
        print('Yes')
        return
    if A[0][2] == A[1][1] == A[2][0] == 0:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()