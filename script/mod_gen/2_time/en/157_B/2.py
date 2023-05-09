def main():
    A = []
    for i in range(3):
        A.append(input().split())
    N = int(input())
    b = [input() for i in range(N)]
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                A[i][j] = 'X'
    for i in range(3):
        if A[i][0] == A[i][1] == A[i][2] == 'X':
            print('Yes')
            return
        if A[0][i] == A[1][i] == A[2][i] == 'X':
            print('Yes')
            return
    if A[0][0] == A[1][1] == A[2][2] == 'X':
        print('Yes')
        return
    if A[0][2] == A[1][1] == A[2][0] == 'X':
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()